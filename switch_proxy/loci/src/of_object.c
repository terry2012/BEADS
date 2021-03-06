/* Copyright (c) 2008 The Board of Trustees of The Leland Stanford Junior University */
/* Copyright (c) 2011, 2012 Open Networking Foundation */
/* Copyright (c) 2012, 2013 Big Switch Networks, Inc. */
/* See the file LICENSE.loci which should have been included in the source distribution */

/****************************************************************
 *
 * of_object.c
 *
 * These are the low level object constructor/destructor operators.
 *
 ****************************************************************/

#include "loci_log.h"
#include <loci/loci.h>
#include <loci/loci_validator.h>

/**
 * Create a generic new object and possibly underlying wire buffer
 * @param bytes The number of bytes to allocate in the underlying buffer
 *
 * If bytes <= 0, do not allocate a wire buffer.
 *
 * Note that this is an internal function.  The class specific
 * new functions should be called to properly initialize and track an
 * OF object.
 */

of_object_t *
of_object_new(int bytes)
{
    of_object_t *obj;

    if ((obj = (of_object_t *)MALLOC(sizeof(*obj))) == NULL) {
        return NULL;
    }
    MEMSET(obj, 0, sizeof(*obj));

    if (bytes > 0) {
        if ((obj->wbuf = of_wire_buffer_new(bytes)) == NULL) {
            FREE(obj);
            return NULL;
        }
    }

    return obj;
}

/**
 * The delete function for LOCI objects
 *
 * @param obj Pointer to the object to be deleted
 *
 * This can be called on any LOCI object; it should not need to be
 * overridden.
 */

void
of_object_delete(of_object_t *obj)
{
    if (obj == NULL) {
        return;
    }

    if (obj->parent == NULL) {
        of_wire_buffer_free(obj->wbuf);
    }

    FREE(obj);
}

/**
 * Duplicate an object
 * @param src The object to be duplicated
 * @returns Pointer to the duplicate or NULL on error.  Caller is responsible
 * for freeing the returned object.
 */

of_object_t *
of_object_dup(of_object_t *src)
{
    of_object_t *dst;
    of_object_init_f init_fn;

    if ((dst = (of_object_t *)MALLOC(sizeof(*dst))) == NULL) {
        return NULL;
    }

    MEMSET(dst, 0, sizeof(*dst));

    /* Allocate a minimal wire buffer assuming we will not write to it. */
    if ((dst->wbuf = of_wire_buffer_new(src->length)) == NULL) {
        FREE(dst);
        return NULL;
    }

    init_fn = of_object_init_map[src->object_id];
    init_fn(dst, src->version, src->length, 0);

    MEMCPY(OF_OBJECT_BUFFER_INDEX(dst, 0),
           OF_OBJECT_BUFFER_INDEX(src, 0),
           src->length);

    return dst;
}

/**
 * Generic new from message call
 */

of_object_t *
of_object_new_from_message(of_message_t msg, int len)
{
    of_object_id_t object_id;
    of_object_t *obj;
    of_version_t version;

    version = of_message_version_get(msg);
    if (!OF_VERSION_OKAY(version)) {
        return NULL;
    }

    if (of_validate_message(msg, len) != 0) {
        LOCI_LOG_ERROR("message validation failed\n");
        return NULL;
    }

    if ((obj = of_object_new(-1)) == NULL) {
        return NULL;
    }

    if (of_object_buffer_bind(obj, OF_MESSAGE_TO_BUFFER(msg), len, 
                              OF_MESSAGE_FREE_FUNCTION) < 0) {
        FREE(obj);
        return NULL;
    }
    obj->version = version;

    of_header_wire_object_id_get(obj, &object_id);
    of_object_init_map[object_id](obj, version, len, 0);

    return obj;
}

/**
 * Parse a message without allocating memory
 *
 * @param storage Pointer to an uninitialized of_object_storage_t
 * @param buf Pointer to the buffer
 * @param length Length of buf
 * @returns Pointer to an initialized of_object_t
 *
 * The lifetime of the returned object is the minimum of the lifetimes of
 * 'buf' and 'storage'.
 */

of_object_t *
of_object_new_from_message_preallocated(of_object_storage_t *storage,
                                        uint8_t *buf, int len)
{
    of_object_t *obj = &storage->obj;
    of_wire_buffer_t *wbuf = &storage->wbuf;
    of_message_t msg = buf;
    of_version_t version;
    of_object_id_t object_id;

    memset(storage, 0, sizeof(*storage));

    version = of_message_version_get(msg);
    if (!OF_VERSION_OKAY(version)) {
        return NULL;
    }

    if (of_validate_message(msg, len) != 0) {
        LOCI_LOG_ERROR("message validation failed\n");
        return NULL;
    }

    obj->version = version;
    obj->wbuf = wbuf;
    wbuf->buf = msg;
    wbuf->alloc_bytes = len;
    wbuf->current_bytes = len;

    of_header_wire_object_id_get(obj, &object_id);
    of_object_init_map[object_id](obj, version, len, 0);

    return obj;
}

/**
 * Bind an existing buffer to an LOCI object
 *
 * @param obj Pointer to the object to be updated
 * @param buf Pointer to the buffer to bind to obj
 * @param bytes Length of buf
 * @param buf_free An optional free function to be applied to
 * buf on deallocation
 *
 * This can be called on any LOCI object; it should not need to be
 * overridden.
 */

int
of_object_buffer_bind(of_object_t *obj, uint8_t *buf, int bytes, 
                      of_buffer_free_f buf_free)
{
    of_wire_buffer_t *wbuf;

    LOCI_ASSERT(buf != NULL);
    LOCI_ASSERT(bytes > 0);

    wbuf = of_wire_buffer_new_bind(buf, bytes, buf_free);
    if (wbuf == NULL) {
        return OF_ERROR_RESOURCE;
    }

    obj->wbuf = wbuf;
    obj->obj_offset = 0;
    obj->length = bytes;

    return OF_ERROR_NONE;
}

/**
 * Connect a child to a parent at the wire buffer level
 *
 * @param parent The top level object to bind to
 * @param child The sub-object connecting to the parent
 * @param offset The offset at which to attach the child RELATIVE 
 * TO THE PARENT in the buffer
 * @param bytes The amount of the buffer dedicated to the child; see below
 * 
 * This is used for 'get' accessors for composite types as well as
 * iterator functions for lists, both read (first/next) and write
 * (append_init, append_advance).
 *
 * Connect a child object to a parent by setting up the child's
 * wire_object to point to the parent's underlying buffer.  The value
 * of the parameter bytes is important in determining how the child
 * is initialized:
 * @li If bytes <= 0, the length and type of the child are not modified;
 * no additional space is added to the buffer.
 * @li If bytes > 0, the current wire buffer is grown to 
 * accomodate this many bytes.  This is to support append operations.
 *
 * If an error is returned, future references to the child object
 * (until it is reinitialized) are undefined.
 */
static void
object_child_attach(of_object_t *parent, of_object_t *child, 
                       int offset, int bytes)
{
    of_object_attach(parent, child, offset, bytes);

    /*
     * bytes determines if this is a read or write setup.
     * If > 0, grow the buffer to accomodate the space
     * Otherwise do nothing
     */
    if (bytes > 0) { /* Set internal length, request buffer space */
        int tot_bytes; /* Total bytes to request for buffer if updated */

        /* Set up space for the child in the parent's buffer */
        tot_bytes = parent->obj_offset + offset + bytes;

        of_wire_buffer_grow(parent->wbuf, tot_bytes);
    }
    /* if bytes == 0 don't do anything */
}

/**
 * Check for room in an object's wire buffer.
 * @param obj The object being checked
 * @param new_len The desired length
 * @return Boolean
 */

int
of_object_can_grow(of_object_t *obj, int new_len)
{
    return OF_OBJECT_ABSOLUTE_OFFSET(obj, new_len) <=
        WBUF_ALLOC_BYTES(obj->wbuf);
}

/**
 * Set the xid of a message object
 * @param obj The object being accessed
 * @param xid The xid value to store in the wire buffer
 * @return OF_ERROR_
 * Since the XID is common across all versions, this is used
 * for all XID accessors.
 */

int
of_object_xid_set(of_object_t *obj, uint32_t xid)
{
    of_wire_buffer_t *wbuf;

    if ((wbuf = OF_OBJECT_TO_WBUF(obj)) == NULL) {
        return OF_ERROR_PARAM;
    }
    of_wire_buffer_u32_set(wbuf, 
        OF_OBJECT_ABSOLUTE_OFFSET(obj, OF_MESSAGE_XID_OFFSET), xid);
    return OF_ERROR_NONE;
}

/**
 * Get the xid of a message object
 * @param obj The object being accessed
 * @param xid Pointer to where to store the xid value
 * @return OF_ERROR_
 * Since the XID is common across all versions, this is used
 * for all XID accessors.
 */

int
of_object_xid_get(of_object_t *obj, uint32_t *xid)
{
    of_wire_buffer_t *wbuf;

    if ((wbuf = OF_OBJECT_TO_WBUF(obj)) == NULL) {
        return OF_ERROR_PARAM;
    }
    of_wire_buffer_u32_get(wbuf, 
        OF_OBJECT_ABSOLUTE_OFFSET(obj, OF_MESSAGE_XID_OFFSET), xid);
    return OF_ERROR_NONE;
}

/****************************************************************
 *
 * Generic list operation implementations
 *
 ****************************************************************/

/**
 * Set up a child for appending to a parent list
 * @param parent The parent; must be a list object
 * @param child The child object; must be of type list element
 * @return OF_ERROR_
 *
 * Attaches the wire buffer of the parent to the child by pointing
 * the child to the end of the parent.
 * 
 * Set the wire length and type from the child.
 * Update the parent length adding the current child length
 *
 * After calling this function, the child object may be updated
 * resulting in changes to the parent's wire buffer
 * 
 */ 

int
of_list_append_bind(of_object_t *parent, of_object_t *child)
{
    if (parent == NULL || child == NULL ||
           parent->wbuf == NULL) {
        return OF_ERROR_PARAM;
    }

    if (!of_object_can_grow(parent, parent->length + child->length)) {
        return OF_ERROR_RESOURCE;
    }

    object_child_attach(parent, child, parent->length, 
                        child->length);

    /* Update the wire length and type if needed */
    of_object_wire_length_set(child, child->length);
    of_object_wire_type_set(child);

    /* Update the parent's length */
    of_object_parent_length_update(parent, child->length);

    OF_LENGTH_CHECK_ASSERT(parent);

    return OF_ERROR_NONE;
}

/**
 * Generic atomic list append operation
 * @param list The list to which an item is being appended
 * @param item THe item to append to the list
 *
 * The contents of the item are copied to the end of the list.
 * Currently assumes the list is at the end of its parent.
 */
int
of_list_append(of_object_t *list, of_object_t *item)
{
    int new_len;

    new_len = list->length + item->length;

    if (!of_object_can_grow(list, new_len)) {
        return OF_ERROR_RESOURCE;
    }

    of_wire_buffer_grow(list->wbuf,
                        OF_OBJECT_ABSOLUTE_OFFSET(list, new_len));

    MEMCPY(OF_OBJECT_BUFFER_INDEX(list, list->length),
           OF_OBJECT_BUFFER_INDEX(item, 0), item->length);

    /* Update the list's length */
    of_object_parent_length_update(list, item->length);

    OF_LENGTH_CHECK_ASSERT(list);

    return OF_ERROR_NONE;
}

/**
 * Generic list first function
 * @param parent The parent; must be a list object
 * @param child The child object; must be of type list element
 * @return OF_ERROR_RANGE if list is empty
 * @return OF_ERROR_
 *
 * Sets up the child to point to the first element in the list
 *
 * Child init must be called before this is called.
 *
 * @note TREAT AS PRIVATE
 * Does not fully initialized object
 */
int
of_list_first(of_object_t *parent, of_object_t *child)
{
    if (parent->length == 0) { /* Empty list */
        return OF_ERROR_RANGE;
    }

    of_object_attach(parent, child, 0, child->length);

    return OF_ERROR_NONE;
}

/**
 * Return boolean indicating if child is pointing to last entry in parent
 * @param parent The parent; must be a list object
 * @param child The child object; must be of type list element
 * @return OF_ERROR_RANGE if list is empty
 * @return OF_ERROR_
 *
 */
static int
of_list_is_last(of_object_t *parent, of_object_t *child)
{
    if (child->obj_offset + child->length >=
        parent->obj_offset + parent->length) {
        return 1;
    }

    return 0;
}

/**
 * Generic list next function
 * @param parent The parent; must be a list object
 * @param child The child object; must be of type list element
 * @return OF_ERROR_RANGE if at end of list
 * @return OF_ERROR_
 *
 * Advances the child to point to the subsequent element in the list.
 * The wire buffer object must not have been modified since the 
 * previous call to _first or _next.
 *
 * @note TREAT AS PRIVATE
 * Does not fully initialized object
 */ 
int
of_list_next(of_object_t *parent, of_object_t *child)
{
    int offset;

    LOCI_ASSERT(child->length > 0);

    /* Get offset of parent */
    if (of_list_is_last(parent, child)) {
        return OF_ERROR_RANGE; /* We were on the last object */
    }

    /* Offset is relative to parent start */
    offset = (child->obj_offset - parent->obj_offset) +
        child->length;
    of_object_attach(parent, child, offset, child->length);

    return OF_ERROR_NONE;
}

void
of_object_wire_buffer_steal(of_object_t *obj, uint8_t **buffer)
{
    LOCI_ASSERT(obj != NULL);
    of_wire_buffer_steal(obj->wbuf, buffer);
    obj->wbuf = NULL;
}

#define _MAX_PARENT_ITERATIONS 8
/**
 * Iteratively update parent lengths thru hierarchy
 * @param obj The object whose length is being updated
 * @param delta The difference between the current and new lengths
 *
 * Note that this includes updating the object itself.  It will
 * iterate thru parents.
 *
 * Assumes delta > 0.
 */
void
of_object_parent_length_update(of_object_t *obj, int delta)
{
#ifndef NDEBUG
    int count = 0;
    of_wire_buffer_t *wbuf;  /* For debug asserts only */
#endif

    while (obj != NULL) {
        LOCI_ASSERT(count++ < _MAX_PARENT_ITERATIONS);
        obj->length += delta;
        of_object_wire_length_set(obj, obj->length);
#ifndef NDEBUG
        wbuf = obj->wbuf;
#endif

        /* Asserts for wire length checking */
        LOCI_ASSERT(obj->length + obj->obj_offset <=
               WBUF_CURRENT_BYTES(wbuf));
        if (obj->parent == NULL) {
            LOCI_ASSERT(obj->length + obj->obj_offset ==
                   WBUF_CURRENT_BYTES(wbuf));
        }

        obj = obj->parent;
    }
}

/**
 * Use the type/length from the wire buffer and init the object
 * @param obj The object being initialized
 * @param base_object_id If > 0, this indicates the base object
 * @param max_len If > 0, the max length to expect for the obj
 * type for inheritance checking
 * @return OF_ERROR_
 *
 * Used for inheritance type objects such as actions and OXMs
 * The type is checked and if valid, the object is initialized.
 * Then the length is taken from the buffer.
 *
 * Note that the object version must already be properly set.
 */
int
of_object_wire_init(of_object_t *obj, of_object_id_t base_object_id,
                    int max_len)
{
    if (loci_class_metadata[obj->object_id].wire_type_get != NULL) {
        of_object_id_t id;
        loci_class_metadata[obj->object_id].wire_type_get(obj, &id);
        obj->object_id = id;
        /* Call the init function for this object type; do not push to wire */
        of_object_init_map[id]((of_object_t *)(obj), obj->version, -1, 0);
    }
    if (loci_class_metadata[obj->object_id].wire_length_get != NULL) {
        int length;
        loci_class_metadata[obj->object_id].wire_length_get(obj, &length);
        if (length < 0 || (max_len > 0 && length > max_len)) {
            return OF_ERROR_PARSE;
        }
        obj->length = length;
    } else {
        /* @fixme Does this cover everything else? */
        obj->length = of_object_fixed_len[obj->version][base_object_id];
    }

    return OF_ERROR_NONE;
}

/*
 * Truncate an object to its initial length.
 *
 * This allows the caller to reuse a single allocated object even if
 * it has been appended to.
 */
void
of_object_truncate(of_object_t *obj)
{
    of_object_init_map[obj->object_id](obj, obj->version, -1, 0);
    obj->wbuf->current_bytes = obj->length;
}
