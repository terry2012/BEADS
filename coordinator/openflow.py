#Samuel Jero <sjero@purdue.edu>
#SDN Testing Strategy Generation
fields_of_aggregate_stats_reply = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'flags', 'type':'uint16'},
	{'name':'packet_count', 'type':'uint64'},
	{'name':'byte_count', 'type':'uint64'},
	{'name':'flow_count', 'type':'uint32'},
]

fields_of_aggregate_stats_request = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'flags', 'type':'uint16'},
	{'name':'table_id', 'type':'uint8'},
	{'name':'out_port', 'type':'uint32'},
	{'name':'out_group', 'type':'uint32'},
	{'name':'cookie', 'type':'uint64'},
	{'name':'cookie_mask', 'type':'uint64'},
	{'name':'match', 'fields': [
		{'name':'version', 'type':'uint8'},
		{'name':'fields', 'fields':[
			{'name':'in_port', 'type':'port'}, #uint32
			{'name':'in_phy_port', 'type':'port'}, #uint32
			{'name':'metadata', 'type':'uint64'},
			{'name':'eth_dst', 'type':'uint48'},
			{'name':'eth_src', 'type':'uint48'},
			{'name':'eth_type', 'type':'uint16'},
			{'name':'vlan_vid', 'type':'uint16'},
			{'name':'vlan_pcp', 'type':'uint8'},
			{'name':'ip_dscp', 'type':'uint8'},
			{'name':'ip_ecn', 'type':'uint8'},
			{'name':'ip_proto', 'type':'uint8'},
			{'name':'ipv4_src', 'type':'uint32'},
			{'name':'ipv4_dst', 'type':'uint32'},
			{'name':'tcp_src', 'type':'uint16'},
			{'name':'tcp_dst', 'type':'uint16'},
			{'name':'udp_src', 'type':'uint16'},
			{'name':'udp_dst', 'type':'uint16'},
			{'name':'sctp_src', 'type':'uint16'},
			{'name':'sctp_dst', 'type':'uint16'},
			{'name':'icmpv4_type', 'type':'uint8'},
			{'name':'icmpv4_code', 'type':'uint8'},
			{'name':'arp_op', 'type':'uint16'},
			{'name':'arp_spa', 'type':'uint32'},
			{'name':'arp_tpa', 'type':'uint32'},
			{'name':'arp_sha', 'type':'uint48'},
			{'name':'arp_tha', 'type':'uint48'},
			{'name':'ipv6_src', 'impl':False, 'type':'uint128'},
			{'name':'ipv6_dst', 'impl':False, 'type':'uint128'},
			{'name':'ipv6_flabel', 'type':'uint32'},
			{'name':'icmpv6_type', 'type':'uint8'},
			{'name':'icmpv6_code', 'type':'uint8'},
			{'name':'ipv6_nd_target', 'impl':False, 'type':'uint128'},
			{'name':'ipv6_nd_sll', 'type':'uint48'},
			{'name':'ipv6_nd_tll', 'type':'uint48'},
			{'name':'mpls_label', 'type':'uint32'},
			{'name':'mpls_tc', 'type':'uint8'},
			{'name':'mpls_bos', 'type':'uint8'},
			{'name':'tunnel_id', 'type':'uint64'},
			{'name':'ipv6_exthdr', 'type':'uint16'},
			{'name':'pbb_uca', 'type':'uint8'},
			{'name':'tunnel_ipv4_src', 'type':'uint32'},
			{'name':'tunnel_ipv4_dst', 'type':'uint32'},
		]},
		{'name':'masks', 'fields':[
			{'name':'in_port', 'type':'uint32'},
			{'name':'in_phy_port', 'type':'uint32'},
			{'name':'metadata', 'type':'uint64'},
			{'name':'eth_dst', 'type':'uint48'},
			{'name':'eth_src', 'type':'uint48'},
			{'name':'eth_type', 'type':'uint16'},
			{'name':'vlan_vid', 'type':'uint16'},
			{'name':'vlan_pcp', 'type':'uint8'},
			{'name':'ip_dscp', 'type':'uint8'},
			{'name':'ip_ecn', 'type':'uint8'},
			{'name':'ip_proto', 'type':'uint8'},
			{'name':'ipv4_src', 'type':'uint32'},
			{'name':'ipv4_dst', 'type':'uint32'},
			{'name':'tcp_src', 'type':'uint16'},
			{'name':'tcp_dst', 'type':'uint16'},
			{'name':'udp_src', 'type':'uint16'},
			{'name':'udp_dst', 'type':'uint16'},
			{'name':'sctp_src', 'type':'uint16'},
			{'name':'sctp_dst', 'type':'uint16'},
			{'name':'icmpv4_type', 'type':'uint8'},
			{'name':'icmpv4_code', 'type':'uint8'},
			{'name':'arp_op', 'type':'uint16'},
			{'name':'arp_spa', 'type':'uint32'},
			{'name':'arp_tpa', 'type':'uint32'},
			{'name':'arp_sha', 'type':'uint48'},
			{'name':'arp_tha', 'type':'uint48'},
			{'name':'ipv6_src', 'impl':False, 'type':'uint128'},
			{'name':'ipv6_dst', 'impl':False, 'type':'uint128'},
			{'name':'ipv6_flabel', 'type':'uint32'},
			{'name':'icmpv6_type', 'type':'uint8'},
			{'name':'icmpv6_code', 'type':'uint8'},
			{'name':'ipv6_nd_target', 'impl':False, 'type':'uint128'},
			{'name':'ipv6_nd_sll', 'type':'uint48'},
			{'name':'ipv6_nd_tll', 'type':'uint48'},
			{'name':'mpls_label', 'type':'uint32'},
			{'name':'mpls_tc', 'type':'uint8'},
			{'name':'mpls_bos', 'type':'uint8'},
			{'name':'tunnel_id', 'type':'uint64'},
			{'name':'ipv6_exthdr', 'type':'uint16'},
			{'name':'pbb_uca', 'type':'uint8'},
			{'name':'tunnel_ipv4_src', 'type':'uint32'},
			{'name':'tunnel_ipv4_dst', 'type':'uint32'},
		]},
	]}
]

fields_of_async_config_failed_error_msg = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'code', 'type':'uint16'},
	{'name':'data', 'impl':False},
]

fields_of_async_get_reply = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'properties', 'fields': [
		##TODO: This Handling is bad
		{'name':'element','type':'TLV', 'fields':[
			{'name':'mask', 'type':'uint32'},
		]},
	]},
	{'name':'packet_in_mask_equal_master', 'type':'uint32'},
	{'name':'packet_in_mask_slave', 'type':'uint32'},
	{'name':'port_status_mask_equal_master', 'type':'uint32'},
	{'name':'port_status_mask_slave', 'type':'uint32'},
	{'name':'flow_removed_mask_equal_master', 'type':'uint32'},
	{'name':'flow_removed_mask_slave', 'type':'uint32'},
]

fields_of_async_get_request = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'properties', 'fields': [
		##TODO: This Handling is bad
		{'name':'element','type':'TLV','fields':[
			{'name':'mask', 'type':'uint32'},
		]},
	]},
	{'name':'packet_in_mask_equal_master', 'type':'uint32'},
	{'name':'packet_in_mask_slave', 'type':'uint32'},
	{'name':'port_status_mask_equal_master', 'type':'uint32'},
	{'name':'port_status_mask_slave', 'type':'uint32'},
	{'name':'flow_removed_mask_equal_master', 'type':'uint32'},
	{'name':'flow_removed_mask_slave', 'type':'uint32'},
]

fields_of_async_set = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'properties', 'fields': [
		##TODO: This Handling is bad
		{'name':'element','type':'TLV','fields':[
			{'name':'mask', 'type':'uint32'},
		]},
	]},
	{'name':'packet_in_mask_equal_master', 'type':'uint32'},
	{'name':'packet_in_mask_slave', 'type':'uint32'},
	{'name':'port_status_mask_equal_master', 'type':'uint32'},
	{'name':'port_status_mask_slave', 'type':'uint32'},
	{'name':'flow_removed_mask_equal_master', 'type':'uint32'},
	{'name':'flow_removed_mask_slave', 'type':'uint32'},
]

fields_of_bad_action_error_msg = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'code', 'type':'uint16'},
	{'name':'data', 'impl':False},
]

fields_of_bad_instruction_error_msg = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'code', 'type':'uint16'},
	{'name':'data', 'impl':False},
]

fields_of_bad_match_error_msg = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'code', 'type':'uint16'},
	{'name':'data', 'impl':False},
]

fields_of_bad_property_error_msg = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'code', 'type':'uint16'},
	{'name':'data', 'impl':False},
]

fields_of_bad_request_error_msg = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'code', 'type':'uint16'},
	{'name':'data', 'impl':False},
]

fields_of_barrier_reply = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
]

fields_of_barrier_request = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
]

fields_of_bundle_add_msg = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'bundle_id', 'type':'uint32'},
	{'name':'flags', 'type':'uint16'},
	{'name':'data', 'impl':False},
]

fields_of_bundle_ctrl_msg = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'bundle_id', 'type':'uint32'},
	{'name':'bundle_ctrl_type', 'type':'uint16'},
	{'name':'flags', 'type':'uint16'},
	{'name':'properties', 'fields': [
		##TODO: This Handling is bad
		{'name':'element','type':'TLV', 'max':2, 'fields':[
			{'name':'seconds', 'type':'uint32'},
			{'name':'nanoseconds', 'type':'uint32'},
		]},
	]},
]

fields_of_bundle_failed_error_msg = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'code', 'type':'uint16'},
	{'name':'data', 'impl':False},
]

fields_of_desc_stats_reply = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'flags', 'type':'uint16'},
	{'name':'mfr_desc', 'impl':False},
	{'name':'hw_desc', 'impl':False},
	{'name':'sw_desc', 'impl':False},
	{'name':'serial_desc', 'impl':False},
	{'name':'dp_desc', 'impl':False},
]

fields_of_desc_stats_request = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'flags', 'type':'uint16'},
]

fields_of_echo_reply = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'data', 'impl':False},
]

fields_of_echo_request = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'data', 'impl':False},
]

fields_of_experimenter = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'experimenter', 'impl':False},
	{'name':'exp_type', 'impl':False},
]

fields_of_experimenter_error_msg = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'code', 'type':'uint16'},
	{'name':'data', 'impl':False},
]

fields_of_experimenter_stats_reply = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'experimenter', 'impl':False},
	{'name':'exp_type', 'impl':False},
]

fields_of_experimenter_stats_request = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'experimenter', 'impl':False},
	{'name':'exp_type', 'impl':False},
]

fields_of_features_reply = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'datapath_id', 'type':'uint64'},
	{'name':'n_buffers', 'type':'uint32'},
	{'name':'n_tables', 'type':'uint8'},
	{'name':'auxilary_id', 'type':'uint8'},
	{'name':'capabilities', 'type':'uint32'},
	{'name':'reserved', 'type':'uint32'},
	{'name':'ports', 'fields':[
		{'name':'element','type':'list', 'fields':[
			{'name':'port_no', 'type':'port'}, #uint32
			{'name':'hw_addr', 'type':'uint48'},
			{'name':'name', 'impl':False},
			{'name':'config', 'type':'uint32'},
			{'name':'state', 'type':'uint32'},
			{'name':'properties', 'fields':[
				##TODO: This Handling is bad
				{'name':'element','type':'TLV', 'max':3, 'fields':[
					{'name':'curr', 'type':'uint32'},
					{'name':'advertised', 'type':'uint32'},
					{'name':'supported', 'type':'uint32'},
					{'name':'peer', 'type':'uint32'},
					{'name':'curr_speed', 'type':'uint32'},
					{'name':'max_speed', 'type':'uint32'},
					{'name':'rx_grid_freq_lmda', 'type':'uint32'},
					{'name':'tx_pwr_min', 'type':'uint32'},
					{'name':'tx_pwr_max', 'type':'uint32'},
				]},
			]},
			{'name':'curr', 'type':'uint32'},
			{'name':'advertised', 'type':'uint32'},
			{'name':'supported', 'type':'uint32'},
			{'name':'peer', 'type':'uint32'},
			{'name':'curr_speed', 'type':'uint32'},
			{'name':'max_speed', 'type':'uint32'},
		]},
	]},
	{'name':'actions', 'type':'uint32'},
]

fields_of_features_request = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
]

fields_of_flow_add = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'cookie', 'type':'uint64'},
	{'name':'cookie_mask', 'type':'uint64'},
	{'name':'table_id', 'type':'uint8'},
	{'name':'idle_timeout', 'type':'uint16'},
	{'name':'hard_timeout', 'type':'uint16'},
	{'name':'priority', 'type':'uint16'},
	{'name':'buffer_id', 'type':'uint32'},
	{'name':'out_port', 'type':'uint32'},
	{'name':'out_group', 'type':'uint32'},
	{'name':'flags', 'type':'uint16'},
	{'name':'importance', 'type':'uint16'},
	{'name':'match', 'fields': [
		{'name':'version', 'type':'uint8'},
		{'name':'fields', 'fields':[
			{'name':'in_port', 'type':'port'}, #uint32
			{'name':'in_phy_port', 'type':'port'}, #uint32
			{'name':'metadata', 'type':'uint64'},
			{'name':'eth_dst', 'type':'uint48'},
			{'name':'eth_src', 'type':'uint48'},
			{'name':'eth_type', 'type':'uint16'},
			{'name':'vlan_vid', 'type':'uint16'},
			{'name':'vlan_pcp', 'type':'uint8'},
			{'name':'ip_dscp', 'type':'uint8'},
			{'name':'ip_ecn', 'type':'uint8'},
			{'name':'ip_proto', 'type':'uint8'},
			{'name':'ipv4_src', 'type':'uint32'},
			{'name':'ipv4_dst', 'type':'uint32'},
			{'name':'tcp_src', 'type':'uint16'},
			{'name':'tcp_dst', 'type':'uint16'},
			{'name':'udp_src', 'type':'uint16'},
			{'name':'udp_dst', 'type':'uint16'},
			{'name':'sctp_src', 'type':'uint16'},
			{'name':'sctp_dst', 'type':'uint16'},
			{'name':'icmpv4_type', 'type':'uint8'},
			{'name':'icmpv4_code', 'type':'uint8'},
			{'name':'arp_op', 'type':'uint16'},
			{'name':'arp_spa', 'type':'uint32'},
			{'name':'arp_tpa', 'type':'uint32'},
			{'name':'arp_sha', 'type':'uint48'},
			{'name':'arp_tha', 'type':'uint48'},
			{'name':'ipv6_src', 'impl':False, 'type':'uint128'},
			{'name':'ipv6_dst', 'impl':False, 'type':'uint128'},
			{'name':'ipv6_flabel', 'type':'uint32'},
			{'name':'icmpv6_type', 'type':'uint8'},
			{'name':'icmpv6_code', 'type':'uint8'},
			{'name':'ipv6_nd_target', 'impl':False, 'type':'uint128'},
			{'name':'ipv6_nd_sll', 'type':'uint48'},
			{'name':'ipv6_nd_tll', 'type':'uint48'},
			{'name':'mpls_label', 'type':'uint32'},
			{'name':'mpls_tc', 'type':'uint8'},
			{'name':'mpls_bos', 'type':'uint8'},
			{'name':'tunnel_id', 'type':'uint64'},
			{'name':'ipv6_exthdr', 'type':'uint16'},
			{'name':'pbb_uca', 'type':'uint8'},
			{'name':'tunnel_ipv4_src', 'type':'uint32'},
			{'name':'tunnel_ipv4_dst', 'type':'uint32'},
		]},
		{'name':'masks', 'fields':[
			{'name':'in_port', 'type':'uint32'},
			{'name':'in_phy_port', 'type':'uint32'},
			{'name':'metadata', 'type':'uint64'},
			{'name':'eth_dst', 'type':'uint48'},
			{'name':'eth_src', 'type':'uint48'},
			{'name':'eth_type', 'type':'uint16'},
			{'name':'vlan_vid', 'type':'uint16'},
			{'name':'vlan_pcp', 'type':'uint8'},
			{'name':'ip_dscp', 'type':'uint8'},
			{'name':'ip_ecn', 'type':'uint8'},
			{'name':'ip_proto', 'type':'uint8'},
			{'name':'ipv4_src', 'type':'uint32'},
			{'name':'ipv4_dst', 'type':'uint32'},
			{'name':'tcp_src', 'type':'uint16'},
			{'name':'tcp_dst', 'type':'uint16'},
			{'name':'udp_src', 'type':'uint16'},
			{'name':'udp_dst', 'type':'uint16'},
			{'name':'sctp_src', 'type':'uint16'},
			{'name':'sctp_dst', 'type':'uint16'},
			{'name':'icmpv4_type', 'type':'uint8'},
			{'name':'icmpv4_code', 'type':'uint8'},
			{'name':'arp_op', 'type':'uint16'},
			{'name':'arp_spa', 'type':'uint32'},
			{'name':'arp_tpa', 'type':'uint32'},
			{'name':'arp_sha', 'type':'uint48'},
			{'name':'arp_tha', 'type':'uint48'},
			{'name':'ipv6_src', 'impl':False, 'type':'uint128'},
			{'name':'ipv6_dst', 'impl':False, 'type':'uint128'},
			{'name':'ipv6_flabel', 'type':'uint32'},
			{'name':'icmpv6_type', 'type':'uint8'},
			{'name':'icmpv6_code', 'type':'uint8'},
			{'name':'ipv6_nd_target', 'impl':False, 'type':'uint128'},
			{'name':'ipv6_nd_sll', 'type':'uint48'},
			{'name':'ipv6_nd_tll', 'type':'uint48'},
			{'name':'mpls_label', 'type':'uint32'},
			{'name':'mpls_tc', 'type':'uint8'},
			{'name':'mpls_bos', 'type':'uint8'},
			{'name':'tunnel_id', 'type':'uint64'},
			{'name':'ipv6_exthdr', 'type':'uint16'},
			{'name':'pbb_uca', 'type':'uint8'},
			{'name':'tunnel_ipv4_src', 'type':'uint32'},
			{'name':'tunnel_ipv4_dst', 'type':'uint32'},
		]},
	]},
	{'name':'instructions', 'fields':[
		##TODO: This Handling is bad
		{'name':'element', 'type':'TLV', 'fields':[
			{'name':'table_id', 'type':'uint48'},
		]},
	]},
	{'name':'actions', 'fields':[
		##TODO: This Handling is bad
		{'name':'element', 'type':'TLV', 'fields':[
			{'name':'port', 'type':'port'}, #uint32
			{'name':'max_len', 'type':'uint16'},
		]},
	]},
]

fields_of_flow_delete = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'cookie', 'type':'uint64'},
	{'name':'cookie_mask', 'type':'uint64'},
	{'name':'table_id', 'type':'uint8'},
	{'name':'idle_timeout', 'type':'uint16'},
	{'name':'hard_timeout', 'type':'uint16'},
	{'name':'priority', 'type':'uint16'},
	{'name':'buffer_id', 'type':'uint32'},
	{'name':'out_port', 'type':'uint32'},
	{'name':'out_group', 'type':'uint32'},
	{'name':'flags', 'type':'uint16'},
	{'name':'importance', 'type':'uint16'},
	{'name':'match', 'fields': [
		{'name':'version', 'type':'uint8'},
		{'name':'fields', 'fields':[
			{'name':'in_port', 'type':'port'}, #uint32
			{'name':'in_phy_port', 'type':'port'}, #uint32
			{'name':'metadata', 'type':'uint64'},
			{'name':'eth_dst', 'type':'uint48'},
			{'name':'eth_src', 'type':'uint48'},
			{'name':'eth_type', 'type':'uint16'},
			{'name':'vlan_vid', 'type':'uint16'},
			{'name':'vlan_pcp', 'type':'uint8'},
			{'name':'ip_dscp', 'type':'uint8'},
			{'name':'ip_ecn', 'type':'uint8'},
			{'name':'ip_proto', 'type':'uint8'},
			{'name':'ipv4_src', 'type':'uint32'},
			{'name':'ipv4_dst', 'type':'uint32'},
			{'name':'tcp_src', 'type':'uint16'},
			{'name':'tcp_dst', 'type':'uint16'},
			{'name':'udp_src', 'type':'uint16'},
			{'name':'udp_dst', 'type':'uint16'},
			{'name':'sctp_src', 'type':'uint16'},
			{'name':'sctp_dst', 'type':'uint16'},
			{'name':'icmpv4_type', 'type':'uint8'},
			{'name':'icmpv4_code', 'type':'uint8'},
			{'name':'arp_op', 'type':'uint16'},
			{'name':'arp_spa', 'type':'uint32'},
			{'name':'arp_tpa', 'type':'uint32'},
			{'name':'arp_sha', 'type':'uint48'},
			{'name':'arp_tha', 'type':'uint48'},
			{'name':'ipv6_src', 'impl':False, 'type':'uint128'},
			{'name':'ipv6_dst', 'impl':False, 'type':'uint128'},
			{'name':'ipv6_flabel', 'type':'uint32'},
			{'name':'icmpv6_type', 'type':'uint8'},
			{'name':'icmpv6_code', 'type':'uint8'},
			{'name':'ipv6_nd_target', 'impl':False, 'type':'uint128'},
			{'name':'ipv6_nd_sll', 'type':'uint48'},
			{'name':'ipv6_nd_tll', 'type':'uint48'},
			{'name':'mpls_label', 'type':'uint32'},
			{'name':'mpls_tc', 'type':'uint8'},
			{'name':'mpls_bos', 'type':'uint8'},
			{'name':'tunnel_id', 'type':'uint64'},
			{'name':'ipv6_exthdr', 'type':'uint16'},
			{'name':'pbb_uca', 'type':'uint8'},
			{'name':'tunnel_ipv4_src', 'type':'uint32'},
			{'name':'tunnel_ipv4_dst', 'type':'uint32'},
		]},
		{'name':'masks', 'fields':[
			{'name':'in_port', 'type':'uint32'},
			{'name':'in_phy_port', 'type':'uint32'},
			{'name':'metadata', 'type':'uint64'},
			{'name':'eth_dst', 'type':'uint48'},
			{'name':'eth_src', 'type':'uint48'},
			{'name':'eth_type', 'type':'uint16'},
			{'name':'vlan_vid', 'type':'uint16'},
			{'name':'vlan_pcp', 'type':'uint8'},
			{'name':'ip_dscp', 'type':'uint8'},
			{'name':'ip_ecn', 'type':'uint8'},
			{'name':'ip_proto', 'type':'uint8'},
			{'name':'ipv4_src', 'type':'uint32'},
			{'name':'ipv4_dst', 'type':'uint32'},
			{'name':'tcp_src', 'type':'uint16'},
			{'name':'tcp_dst', 'type':'uint16'},
			{'name':'udp_src', 'type':'uint16'},
			{'name':'udp_dst', 'type':'uint16'},
			{'name':'sctp_src', 'type':'uint16'},
			{'name':'sctp_dst', 'type':'uint16'},
			{'name':'icmpv4_type', 'type':'uint8'},
			{'name':'icmpv4_code', 'type':'uint8'},
			{'name':'arp_op', 'type':'uint16'},
			{'name':'arp_spa', 'type':'uint32'},
			{'name':'arp_tpa', 'type':'uint32'},
			{'name':'arp_sha', 'type':'uint48'},
			{'name':'arp_tha', 'type':'uint48'},
			{'name':'ipv6_src', 'impl':False, 'type':'uint128'},
			{'name':'ipv6_dst', 'impl':False, 'type':'uint128'},
			{'name':'ipv6_flabel', 'type':'uint32'},
			{'name':'icmpv6_type', 'type':'uint8'},
			{'name':'icmpv6_code', 'type':'uint8'},
			{'name':'ipv6_nd_target', 'impl':False, 'type':'uint128'},
			{'name':'ipv6_nd_sll', 'type':'uint48'},
			{'name':'ipv6_nd_tll', 'type':'uint48'},
			{'name':'mpls_label', 'type':'uint32'},
			{'name':'mpls_tc', 'type':'uint8'},
			{'name':'mpls_bos', 'type':'uint8'},
			{'name':'tunnel_id', 'type':'uint64'},
			{'name':'ipv6_exthdr', 'type':'uint16'},
			{'name':'pbb_uca', 'type':'uint8'},
			{'name':'tunnel_ipv4_src', 'type':'uint32'},
			{'name':'tunnel_ipv4_dst', 'type':'uint32'},
		]},
	]},
	{'name':'instructions', 'fields':[
		##TODO: This Handling is bad
		{'name':'element', 'type':'TLV', 'fields':[
			{'name':'table_id', 'type':'uint48'},
		]},
	]},
	{'name':'actions', 'fields':[
		##TODO: This Handling is bad
		{'name':'element', 'type':'TLV', 'fields':[
			{'name':'port', 'type':'port'}, #uint32
			{'name':'max_len', 'type':'uint16'},
		]},
	]},
]

fields_of_flow_delete_strict = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'cookie', 'type':'uint64'},
	{'name':'cookie_mask', 'type':'uint64'},
	{'name':'table_id', 'type':'uint8'},
	{'name':'idle_timeout', 'type':'uint16'},
	{'name':'hard_timeout', 'type':'uint16'},
	{'name':'priority', 'type':'uint16'},
	{'name':'buffer_id', 'type':'uint32'},
	{'name':'out_port', 'type':'uint32'},
	{'name':'out_group', 'type':'uint32'},
	{'name':'flags', 'type':'uint16'},
	{'name':'importance', 'type':'uint16'},
	{'name':'match', 'fields': [
		{'name':'version', 'type':'uint8'},
		{'name':'fields', 'fields':[
			{'name':'in_port', 'type':'port'}, #uint32
			{'name':'in_phy_port', 'type':'port'}, #uint32
			{'name':'metadata', 'type':'uint64'},
			{'name':'eth_dst', 'type':'uint48'},
			{'name':'eth_src', 'type':'uint48'},
			{'name':'eth_type', 'type':'uint16'},
			{'name':'vlan_vid', 'type':'uint16'},
			{'name':'vlan_pcp', 'type':'uint8'},
			{'name':'ip_dscp', 'type':'uint8'},
			{'name':'ip_ecn', 'type':'uint8'},
			{'name':'ip_proto', 'type':'uint8'},
			{'name':'ipv4_src', 'type':'uint32'},
			{'name':'ipv4_dst', 'type':'uint32'},
			{'name':'tcp_src', 'type':'uint16'},
			{'name':'tcp_dst', 'type':'uint16'},
			{'name':'udp_src', 'type':'uint16'},
			{'name':'udp_dst', 'type':'uint16'},
			{'name':'sctp_src', 'type':'uint16'},
			{'name':'sctp_dst', 'type':'uint16'},
			{'name':'icmpv4_type', 'type':'uint8'},
			{'name':'icmpv4_code', 'type':'uint8'},
			{'name':'arp_op', 'type':'uint16'},
			{'name':'arp_spa', 'type':'uint32'},
			{'name':'arp_tpa', 'type':'uint32'},
			{'name':'arp_sha', 'type':'uint48'},
			{'name':'arp_tha', 'type':'uint48'},
			{'name':'ipv6_src', 'impl':False, 'type':'uint128'},
			{'name':'ipv6_dst', 'impl':False, 'type':'uint128'},
			{'name':'ipv6_flabel', 'type':'uint32'},
			{'name':'icmpv6_type', 'type':'uint8'},
			{'name':'icmpv6_code', 'type':'uint8'},
			{'name':'ipv6_nd_target', 'impl':False, 'type':'uint128'},
			{'name':'ipv6_nd_sll', 'type':'uint48'},
			{'name':'ipv6_nd_tll', 'type':'uint48'},
			{'name':'mpls_label', 'type':'uint32'},
			{'name':'mpls_tc', 'type':'uint8'},
			{'name':'mpls_bos', 'type':'uint8'},
			{'name':'tunnel_id', 'type':'uint64'},
			{'name':'ipv6_exthdr', 'type':'uint16'},
			{'name':'pbb_uca', 'type':'uint8'},
			{'name':'tunnel_ipv4_src', 'type':'uint32'},
			{'name':'tunnel_ipv4_dst', 'type':'uint32'},
		]},
		{'name':'masks', 'fields':[
			{'name':'in_port', 'type':'uint32'},
			{'name':'in_phy_port', 'type':'uint32'},
			{'name':'metadata', 'type':'uint64'},
			{'name':'eth_dst', 'type':'uint48'},
			{'name':'eth_src', 'type':'uint48'},
			{'name':'eth_type', 'type':'uint16'},
			{'name':'vlan_vid', 'type':'uint16'},
			{'name':'vlan_pcp', 'type':'uint8'},
			{'name':'ip_dscp', 'type':'uint8'},
			{'name':'ip_ecn', 'type':'uint8'},
			{'name':'ip_proto', 'type':'uint8'},
			{'name':'ipv4_src', 'type':'uint32'},
			{'name':'ipv4_dst', 'type':'uint32'},
			{'name':'tcp_src', 'type':'uint16'},
			{'name':'tcp_dst', 'type':'uint16'},
			{'name':'udp_src', 'type':'uint16'},
			{'name':'udp_dst', 'type':'uint16'},
			{'name':'sctp_src', 'type':'uint16'},
			{'name':'sctp_dst', 'type':'uint16'},
			{'name':'icmpv4_type', 'type':'uint8'},
			{'name':'icmpv4_code', 'type':'uint8'},
			{'name':'arp_op', 'type':'uint16'},
			{'name':'arp_spa', 'type':'uint32'},
			{'name':'arp_tpa', 'type':'uint32'},
			{'name':'arp_sha', 'type':'uint48'},
			{'name':'arp_tha', 'type':'uint48'},
			{'name':'ipv6_src', 'impl':False, 'type':'uint128'},
			{'name':'ipv6_dst', 'impl':False, 'type':'uint128'},
			{'name':'ipv6_flabel', 'type':'uint32'},
			{'name':'icmpv6_type', 'type':'uint8'},
			{'name':'icmpv6_code', 'type':'uint8'},
			{'name':'ipv6_nd_target', 'impl':False, 'type':'uint128'},
			{'name':'ipv6_nd_sll', 'type':'uint48'},
			{'name':'ipv6_nd_tll', 'type':'uint48'},
			{'name':'mpls_label', 'type':'uint32'},
			{'name':'mpls_tc', 'type':'uint8'},
			{'name':'mpls_bos', 'type':'uint8'},
			{'name':'tunnel_id', 'type':'uint64'},
			{'name':'ipv6_exthdr', 'type':'uint16'},
			{'name':'pbb_uca', 'type':'uint8'},
			{'name':'tunnel_ipv4_src', 'type':'uint32'},
			{'name':'tunnel_ipv4_dst', 'type':'uint32'},
		]},
	]},
	{'name':'instructions', 'fields':[
		##TODO: This Handling is bad
		{'name':'element', 'type':'TLV', 'fields':[
			{'name':'table_id', 'type':'uint48'},
		]},
	]},
	{'name':'actions', 'fields':[
		##TODO: This Handling is bad
		{'name':'element', 'type':'TLV', 'fields':[
			{'name':'port', 'type':'port'}, #uint32
			{'name':'max_len', 'type':'uint16'},
		]},
	]},
]

fields_of_flow_modify = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'cookie', 'type':'uint64'},
	{'name':'cookie_mask', 'type':'uint64'},
	{'name':'table_id', 'type':'uint8'},
	{'name':'idle_timeout', 'type':'uint16'},
	{'name':'hard_timeout', 'type':'uint16'},
	{'name':'priority', 'type':'uint16'},
	{'name':'buffer_id', 'type':'uint32'},
	{'name':'out_port', 'type':'uint32'},
	{'name':'out_group', 'type':'uint32'},
	{'name':'flags', 'type':'uint16'},
	{'name':'importance', 'type':'uint16'},
	{'name':'match', 'fields': [
		{'name':'version', 'type':'uint8'},
		{'name':'fields', 'fields':[
			{'name':'in_port', 'type':'port'}, #uint32
			{'name':'in_phy_port', 'type':'port'}, #uint32
			{'name':'metadata', 'type':'uint64'},
			{'name':'eth_dst', 'type':'uint48'},
			{'name':'eth_src', 'type':'uint48'},
			{'name':'eth_type', 'type':'uint16'},
			{'name':'vlan_vid', 'type':'uint16'},
			{'name':'vlan_pcp', 'type':'uint8'},
			{'name':'ip_dscp', 'type':'uint8'},
			{'name':'ip_ecn', 'type':'uint8'},
			{'name':'ip_proto', 'type':'uint8'},
			{'name':'ipv4_src', 'type':'uint32'},
			{'name':'ipv4_dst', 'type':'uint32'},
			{'name':'tcp_src', 'type':'uint16'},
			{'name':'tcp_dst', 'type':'uint16'},
			{'name':'udp_src', 'type':'uint16'},
			{'name':'udp_dst', 'type':'uint16'},
			{'name':'sctp_src', 'type':'uint16'},
			{'name':'sctp_dst', 'type':'uint16'},
			{'name':'icmpv4_type', 'type':'uint8'},
			{'name':'icmpv4_code', 'type':'uint8'},
			{'name':'arp_op', 'type':'uint16'},
			{'name':'arp_spa', 'type':'uint32'},
			{'name':'arp_tpa', 'type':'uint32'},
			{'name':'arp_sha', 'type':'uint48'},
			{'name':'arp_tha', 'type':'uint48'},
			{'name':'ipv6_src', 'impl':False, 'type':'uint128'},
			{'name':'ipv6_dst', 'impl':False, 'type':'uint128'},
			{'name':'ipv6_flabel', 'type':'uint32'},
			{'name':'icmpv6_type', 'type':'uint8'},
			{'name':'icmpv6_code', 'type':'uint8'},
			{'name':'ipv6_nd_target', 'impl':False, 'type':'uint128'},
			{'name':'ipv6_nd_sll', 'type':'uint48'},
			{'name':'ipv6_nd_tll', 'type':'uint48'},
			{'name':'mpls_label', 'type':'uint32'},
			{'name':'mpls_tc', 'type':'uint8'},
			{'name':'mpls_bos', 'type':'uint8'},
			{'name':'tunnel_id', 'type':'uint64'},
			{'name':'ipv6_exthdr', 'type':'uint16'},
			{'name':'pbb_uca', 'type':'uint8'},
			{'name':'tunnel_ipv4_src', 'type':'uint32'},
			{'name':'tunnel_ipv4_dst', 'type':'uint32'},
		]},
		{'name':'masks', 'fields':[
			{'name':'in_port', 'type':'uint32'},
			{'name':'in_phy_port', 'type':'uint32'},
			{'name':'metadata', 'type':'uint64'},
			{'name':'eth_dst', 'type':'uint48'},
			{'name':'eth_src', 'type':'uint48'},
			{'name':'eth_type', 'type':'uint16'},
			{'name':'vlan_vid', 'type':'uint16'},
			{'name':'vlan_pcp', 'type':'uint8'},
			{'name':'ip_dscp', 'type':'uint8'},
			{'name':'ip_ecn', 'type':'uint8'},
			{'name':'ip_proto', 'type':'uint8'},
			{'name':'ipv4_src', 'type':'uint32'},
			{'name':'ipv4_dst', 'type':'uint32'},
			{'name':'tcp_src', 'type':'uint16'},
			{'name':'tcp_dst', 'type':'uint16'},
			{'name':'udp_src', 'type':'uint16'},
			{'name':'udp_dst', 'type':'uint16'},
			{'name':'sctp_src', 'type':'uint16'},
			{'name':'sctp_dst', 'type':'uint16'},
			{'name':'icmpv4_type', 'type':'uint8'},
			{'name':'icmpv4_code', 'type':'uint8'},
			{'name':'arp_op', 'type':'uint16'},
			{'name':'arp_spa', 'type':'uint32'},
			{'name':'arp_tpa', 'type':'uint32'},
			{'name':'arp_sha', 'type':'uint48'},
			{'name':'arp_tha', 'type':'uint48'},
			{'name':'ipv6_src', 'impl':False, 'type':'uint128'},
			{'name':'ipv6_dst', 'impl':False, 'type':'uint128'},
			{'name':'ipv6_flabel', 'type':'uint32'},
			{'name':'icmpv6_type', 'type':'uint8'},
			{'name':'icmpv6_code', 'type':'uint8'},
			{'name':'ipv6_nd_target', 'impl':False, 'type':'uint128'},
			{'name':'ipv6_nd_sll', 'type':'uint48'},
			{'name':'ipv6_nd_tll', 'type':'uint48'},
			{'name':'mpls_label', 'type':'uint32'},
			{'name':'mpls_tc', 'type':'uint8'},
			{'name':'mpls_bos', 'type':'uint8'},
			{'name':'tunnel_id', 'type':'uint64'},
			{'name':'ipv6_exthdr', 'type':'uint16'},
			{'name':'pbb_uca', 'type':'uint8'},
			{'name':'tunnel_ipv4_src', 'type':'uint32'},
			{'name':'tunnel_ipv4_dst', 'type':'uint32'},
		]},
	]},
	{'name':'instructions', 'fields':[
		##TODO: This Handling is bad
		{'name':'element', 'type':'TLV', 'fields':[
			{'name':'table_id', 'type':'uint48'},
		]},
	]},
	{'name':'actions', 'fields':[
		##TODO: This Handling is bad
		{'name':'element', 'type':'TLV', 'fields':[
			{'name':'port', 'type':'port'}, #uint32
			{'name':'max_len', 'type':'uint16'},
		]},
	]},
]

fields_of_flow_modify_strict = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'cookie', 'type':'uint64'},
	{'name':'cookie_mask', 'type':'uint64'},
	{'name':'table_id', 'type':'uint8'},
	{'name':'idle_timeout', 'type':'uint16'},
	{'name':'hard_timeout', 'type':'uint16'},
	{'name':'priority', 'type':'uint16'},
	{'name':'buffer_id', 'type':'uint32'},
	{'name':'out_port', 'type':'uint32'},
	{'name':'out_group', 'type':'uint32'},
	{'name':'flags', 'type':'uint16'},
	{'name':'importance', 'type':'uint16'},
	{'name':'match', 'fields': [
		{'name':'version', 'type':'uint8'},
		{'name':'fields', 'fields':[
			{'name':'in_port', 'type':'port'}, #uint32
			{'name':'in_phy_port', 'type':'port'}, #uint32
			{'name':'metadata', 'type':'uint64'},
			{'name':'eth_dst', 'type':'uint48'},
			{'name':'eth_src', 'type':'uint48'},
			{'name':'eth_type', 'type':'uint16'},
			{'name':'vlan_vid', 'type':'uint16'},
			{'name':'vlan_pcp', 'type':'uint8'},
			{'name':'ip_dscp', 'type':'uint8'},
			{'name':'ip_ecn', 'type':'uint8'},
			{'name':'ip_proto', 'type':'uint8'},
			{'name':'ipv4_src', 'type':'uint32'},
			{'name':'ipv4_dst', 'type':'uint32'},
			{'name':'tcp_src', 'type':'uint16'},
			{'name':'tcp_dst', 'type':'uint16'},
			{'name':'udp_src', 'type':'uint16'},
			{'name':'udp_dst', 'type':'uint16'},
			{'name':'sctp_src', 'type':'uint16'},
			{'name':'sctp_dst', 'type':'uint16'},
			{'name':'icmpv4_type', 'type':'uint8'},
			{'name':'icmpv4_code', 'type':'uint8'},
			{'name':'arp_op', 'type':'uint16'},
			{'name':'arp_spa', 'type':'uint32'},
			{'name':'arp_tpa', 'type':'uint32'},
			{'name':'arp_sha', 'type':'uint48'},
			{'name':'arp_tha', 'type':'uint48'},
			{'name':'ipv6_src', 'impl':False, 'type':'uint128'},
			{'name':'ipv6_dst', 'impl':False, 'type':'uint128'},
			{'name':'ipv6_flabel', 'type':'uint32'},
			{'name':'icmpv6_type', 'type':'uint8'},
			{'name':'icmpv6_code', 'type':'uint8'},
			{'name':'ipv6_nd_target', 'impl':False, 'type':'uint128'},
			{'name':'ipv6_nd_sll', 'type':'uint48'},
			{'name':'ipv6_nd_tll', 'type':'uint48'},
			{'name':'mpls_label', 'type':'uint32'},
			{'name':'mpls_tc', 'type':'uint8'},
			{'name':'mpls_bos', 'type':'uint8'},
			{'name':'tunnel_id', 'type':'uint64'},
			{'name':'ipv6_exthdr', 'type':'uint16'},
			{'name':'pbb_uca', 'type':'uint8'},
			{'name':'tunnel_ipv4_src', 'type':'uint32'},
			{'name':'tunnel_ipv4_dst', 'type':'uint32'},
		]},
		{'name':'masks', 'fields':[
			{'name':'in_port', 'type':'uint32'},
			{'name':'in_phy_port', 'type':'uint32'},
			{'name':'metadata', 'type':'uint64'},
			{'name':'eth_dst', 'type':'uint48'},
			{'name':'eth_src', 'type':'uint48'},
			{'name':'eth_type', 'type':'uint16'},
			{'name':'vlan_vid', 'type':'uint16'},
			{'name':'vlan_pcp', 'type':'uint8'},
			{'name':'ip_dscp', 'type':'uint8'},
			{'name':'ip_ecn', 'type':'uint8'},
			{'name':'ip_proto', 'type':'uint8'},
			{'name':'ipv4_src', 'type':'uint32'},
			{'name':'ipv4_dst', 'type':'uint32'},
			{'name':'tcp_src', 'type':'uint16'},
			{'name':'tcp_dst', 'type':'uint16'},
			{'name':'udp_src', 'type':'uint16'},
			{'name':'udp_dst', 'type':'uint16'},
			{'name':'sctp_src', 'type':'uint16'},
			{'name':'sctp_dst', 'type':'uint16'},
			{'name':'icmpv4_type', 'type':'uint8'},
			{'name':'icmpv4_code', 'type':'uint8'},
			{'name':'arp_op', 'type':'uint16'},
			{'name':'arp_spa', 'type':'uint32'},
			{'name':'arp_tpa', 'type':'uint32'},
			{'name':'arp_sha', 'type':'uint48'},
			{'name':'arp_tha', 'type':'uint48'},
			{'name':'ipv6_src', 'impl':False, 'type':'uint128'},
			{'name':'ipv6_dst', 'impl':False, 'type':'uint128'},
			{'name':'ipv6_flabel', 'type':'uint32'},
			{'name':'icmpv6_type', 'type':'uint8'},
			{'name':'icmpv6_code', 'type':'uint8'},
			{'name':'ipv6_nd_target', 'impl':False, 'type':'uint128'},
			{'name':'ipv6_nd_sll', 'type':'uint48'},
			{'name':'ipv6_nd_tll', 'type':'uint48'},
			{'name':'mpls_label', 'type':'uint32'},
			{'name':'mpls_tc', 'type':'uint8'},
			{'name':'mpls_bos', 'type':'uint8'},
			{'name':'tunnel_id', 'type':'uint64'},
			{'name':'ipv6_exthdr', 'type':'uint16'},
			{'name':'pbb_uca', 'type':'uint8'},
			{'name':'tunnel_ipv4_src', 'type':'uint32'},
			{'name':'tunnel_ipv4_dst', 'type':'uint32'},
		]},
	]},
	{'name':'instructions', 'fields':[
		##TODO: This Handling is bad
		{'name':'element', 'type':'TLV', 'fields':[
			{'name':'table_id', 'type':'uint48'},
		]},
	]},
	{'name':'actions', 'fields':[
		##TODO: This Handling is bad
		{'name':'element', 'type':'TLV', 'fields':[
			{'name':'port', 'type':'port'}, #uint32
			{'name':'max_len', 'type':'uint16'},
		]},
	]},
]

fields_of_flow_mod_failed_error_msg = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'code', 'type':'uint16'},
	{'name':'data', 'impl':False},
]

fields_of_flow_monitor_failed_error_msg = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'code', 'type':'uint16'},
	{'name':'data', 'impl':False},
]

fields_of_flow_removed = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'cookie', 'type':'uint64'},
	{'name':'priority', 'type':'uint16'},
	{'name':'reason', 'type':'uint8'},
	{'name':'table_id', 'type':'uint8'},
	{'name':'duration_sec', 'type':'uint32'},
	{'name':'duration_nsec', 'type':'uint32'},
	{'name':'idle_timeout', 'type':'uint16'},
	{'name':'hard_timeout', 'type':'uint16'},
	{'name':'packet_count', 'type':'uint64'},
	{'name':'byte_count', 'type':'uint64'},
	{'name':'match', 'fields': [
		{'name':'version', 'type':'uint8'},
		{'name':'fields', 'fields':[
			{'name':'in_port', 'type':'port'}, #uint32
			{'name':'in_phy_port', 'type':'port'}, #uint32
			{'name':'metadata', 'type':'uint64'},
			{'name':'eth_dst', 'type':'uint48'},
			{'name':'eth_src', 'type':'uint48'},
			{'name':'eth_type', 'type':'uint16'},
			{'name':'vlan_vid', 'type':'uint16'},
			{'name':'vlan_pcp', 'type':'uint8'},
			{'name':'ip_dscp', 'type':'uint8'},
			{'name':'ip_ecn', 'type':'uint8'},
			{'name':'ip_proto', 'type':'uint8'},
			{'name':'ipv4_src', 'type':'uint32'},
			{'name':'ipv4_dst', 'type':'uint32'},
			{'name':'tcp_src', 'type':'uint16'},
			{'name':'tcp_dst', 'type':'uint16'},
			{'name':'udp_src', 'type':'uint16'},
			{'name':'udp_dst', 'type':'uint16'},
			{'name':'sctp_src', 'type':'uint16'},
			{'name':'sctp_dst', 'type':'uint16'},
			{'name':'icmpv4_type', 'type':'uint8'},
			{'name':'icmpv4_code', 'type':'uint8'},
			{'name':'arp_op', 'type':'uint16'},
			{'name':'arp_spa', 'type':'uint32'},
			{'name':'arp_tpa', 'type':'uint32'},
			{'name':'arp_sha', 'type':'uint48'},
			{'name':'arp_tha', 'type':'uint48'},
			{'name':'ipv6_src', 'impl':False, 'type':'uint128'},
			{'name':'ipv6_dst', 'impl':False, 'type':'uint128'},
			{'name':'ipv6_flabel', 'type':'uint32'},
			{'name':'icmpv6_type', 'type':'uint8'},
			{'name':'icmpv6_code', 'type':'uint8'},
			{'name':'ipv6_nd_target', 'impl':False, 'type':'uint128'},
			{'name':'ipv6_nd_sll', 'type':'uint48'},
			{'name':'ipv6_nd_tll', 'type':'uint48'},
			{'name':'mpls_label', 'type':'uint32'},
			{'name':'mpls_tc', 'type':'uint8'},
			{'name':'mpls_bos', 'type':'uint8'},
			{'name':'tunnel_id', 'type':'uint64'},
			{'name':'ipv6_exthdr', 'type':'uint16'},
			{'name':'pbb_uca', 'type':'uint8'},
			{'name':'tunnel_ipv4_src', 'type':'uint32'},
			{'name':'tunnel_ipv4_dst', 'type':'uint32'},
		]},
		{'name':'masks', 'fields':[
			{'name':'in_port', 'type':'uint32'},
			{'name':'in_phy_port', 'type':'uint32'},
			{'name':'metadata', 'type':'uint64'},
			{'name':'eth_dst', 'type':'uint48'},
			{'name':'eth_src', 'type':'uint48'},
			{'name':'eth_type', 'type':'uint16'},
			{'name':'vlan_vid', 'type':'uint16'},
			{'name':'vlan_pcp', 'type':'uint8'},
			{'name':'ip_dscp', 'type':'uint8'},
			{'name':'ip_ecn', 'type':'uint8'},
			{'name':'ip_proto', 'type':'uint8'},
			{'name':'ipv4_src', 'type':'uint32'},
			{'name':'ipv4_dst', 'type':'uint32'},
			{'name':'tcp_src', 'type':'uint16'},
			{'name':'tcp_dst', 'type':'uint16'},
			{'name':'udp_src', 'type':'uint16'},
			{'name':'udp_dst', 'type':'uint16'},
			{'name':'sctp_src', 'type':'uint16'},
			{'name':'sctp_dst', 'type':'uint16'},
			{'name':'icmpv4_type', 'type':'uint8'},
			{'name':'icmpv4_code', 'type':'uint8'},
			{'name':'arp_op', 'type':'uint16'},
			{'name':'arp_spa', 'type':'uint32'},
			{'name':'arp_tpa', 'type':'uint32'},
			{'name':'arp_sha', 'type':'uint48'},
			{'name':'arp_tha', 'type':'uint48'},
			{'name':'ipv6_src', 'impl':False, 'type':'uint128'},
			{'name':'ipv6_dst', 'impl':False, 'type':'uint128'},
			{'name':'ipv6_flabel', 'type':'uint32'},
			{'name':'icmpv6_type', 'type':'uint8'},
			{'name':'icmpv6_code', 'type':'uint8'},
			{'name':'ipv6_nd_target', 'impl':False, 'type':'uint128'},
			{'name':'ipv6_nd_sll', 'type':'uint48'},
			{'name':'ipv6_nd_tll', 'type':'uint48'},
			{'name':'mpls_label', 'type':'uint32'},
			{'name':'mpls_tc', 'type':'uint8'},
			{'name':'mpls_bos', 'type':'uint8'},
			{'name':'tunnel_id', 'type':'uint64'},
			{'name':'ipv6_exthdr', 'type':'uint16'},
			{'name':'pbb_uca', 'type':'uint8'},
			{'name':'tunnel_ipv4_src', 'type':'uint32'},
			{'name':'tunnel_ipv4_dst', 'type':'uint32'},
		]},
	]},
]

fields_of_flow_stats_reply = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'flags', 'type':'uint16'},
	{'name':'entries', 'fields':[
		{'name':'element','type':'list', 'fields':[
			{'name':'table_id', 'type':'uint8'},
			{'name':'duration_sec', 'type':'uint64'},
			{'name':'duration_nsec', 'type':'uint64'},
			{'name':'priority', 'type':'uint16'},
			{'name':'idle_timeout', 'type':'uint16'},
			{'name':'hard_timeout', 'type':'uint16'},
			{'name':'flags', 'type':'uint16'},
			{'name':'importance', 'type':'uint16'},
			{'name':'cookie', 'type':'uint32'},
			{'name':'packet_count', 'type':'uint64'},
			{'name':'byte_count', 'type':'uint64'},
			{'name':'match', 'fields': [
				{'name':'version', 'type':'uint8'},
				{'name':'fields', 'fields':[
					{'name':'in_port', 'type':'port'}, #uint32
					{'name':'in_phy_port', 'type':'port'}, #uint32
					{'name':'metadata', 'type':'uint64'},
					{'name':'eth_dst', 'type':'uint48'},
					{'name':'eth_src', 'type':'uint48'},
					{'name':'eth_type', 'type':'uint16'},
					{'name':'vlan_vid', 'type':'uint16'},
					{'name':'vlan_pcp', 'type':'uint8'},
					{'name':'ip_dscp', 'type':'uint8'},
					{'name':'ip_ecn', 'type':'uint8'},
					{'name':'ip_proto', 'type':'uint8'},
					{'name':'ipv4_src', 'type':'uint32'},
					{'name':'ipv4_dst', 'type':'uint32'},
					{'name':'tcp_src', 'type':'uint16'},
					{'name':'tcp_dst', 'type':'uint16'},
					{'name':'udp_src', 'type':'uint16'},
					{'name':'udp_dst', 'type':'uint16'},
					{'name':'sctp_src', 'type':'uint16'},
					{'name':'sctp_dst', 'type':'uint16'},
					{'name':'icmpv4_type', 'type':'uint8'},
					{'name':'icmpv4_code', 'type':'uint8'},
					{'name':'arp_op', 'type':'uint16'},
					{'name':'arp_spa', 'type':'uint32'},
					{'name':'arp_tpa', 'type':'uint32'},
					{'name':'arp_sha', 'type':'uint48'},
					{'name':'arp_tha', 'type':'uint48'},
					{'name':'ipv6_src', 'impl':False, 'type':'uint128'},
					{'name':'ipv6_dst', 'impl':False, 'type':'uint128'},
					{'name':'ipv6_flabel', 'type':'uint32'},
					{'name':'icmpv6_type', 'type':'uint8'},
					{'name':'icmpv6_code', 'type':'uint8'},
					{'name':'ipv6_nd_target', 'impl':False, 'type':'uint128'},
					{'name':'ipv6_nd_sll', 'type':'uint48'},
					{'name':'ipv6_nd_tll', 'type':'uint48'},
					{'name':'mpls_label', 'type':'uint32'},
					{'name':'mpls_tc', 'type':'uint8'},
					{'name':'mpls_bos', 'type':'uint8'},
					{'name':'tunnel_id', 'type':'uint64'},
					{'name':'ipv6_exthdr', 'type':'uint16'},
					{'name':'pbb_uca', 'type':'uint8'},
					{'name':'tunnel_ipv4_src', 'type':'uint32'},
					{'name':'tunnel_ipv4_dst', 'type':'uint32'},
				]},
				{'name':'masks', 'fields':[
					{'name':'in_port', 'type':'uint32'},
					{'name':'in_phy_port', 'type':'uint32'},
					{'name':'metadata', 'type':'uint64'},
					{'name':'eth_dst', 'type':'uint48'},
					{'name':'eth_src', 'type':'uint48'},
					{'name':'eth_type', 'type':'uint16'},
					{'name':'vlan_vid', 'type':'uint16'},
					{'name':'vlan_pcp', 'type':'uint8'},
					{'name':'ip_dscp', 'type':'uint8'},
					{'name':'ip_ecn', 'type':'uint8'},
					{'name':'ip_proto', 'type':'uint8'},
					{'name':'ipv4_src', 'type':'uint32'},
					{'name':'ipv4_dst', 'type':'uint32'},
					{'name':'tcp_src', 'type':'uint16'},
					{'name':'tcp_dst', 'type':'uint16'},
					{'name':'udp_src', 'type':'uint16'},
					{'name':'udp_dst', 'type':'uint16'},
					{'name':'sctp_src', 'type':'uint16'},
					{'name':'sctp_dst', 'type':'uint16'},
					{'name':'icmpv4_type', 'type':'uint8'},
					{'name':'icmpv4_code', 'type':'uint8'},
					{'name':'arp_op', 'type':'uint16'},
					{'name':'arp_spa', 'type':'uint32'},
					{'name':'arp_tpa', 'type':'uint32'},
					{'name':'arp_sha', 'type':'uint48'},
					{'name':'arp_tha', 'type':'uint48'},
					{'name':'ipv6_src', 'impl':False, 'type':'uint128'},
					{'name':'ipv6_dst', 'impl':False, 'type':'uint128'},
					{'name':'ipv6_flabel', 'type':'uint32'},
					{'name':'icmpv6_type', 'type':'uint8'},
					{'name':'icmpv6_code', 'type':'uint8'},
					{'name':'ipv6_nd_target', 'impl':False, 'type':'uint128'},
					{'name':'ipv6_nd_sll', 'type':'uint48'},
					{'name':'ipv6_nd_tll', 'type':'uint48'},
					{'name':'mpls_label', 'type':'uint32'},
					{'name':'mpls_tc', 'type':'uint8'},
					{'name':'mpls_bos', 'type':'uint8'},
					{'name':'tunnel_id', 'type':'uint64'},
					{'name':'ipv6_exthdr', 'type':'uint16'},
					{'name':'pbb_uca', 'type':'uint8'},
					{'name':'tunnel_ipv4_src', 'type':'uint32'},
					{'name':'tunnel_ipv4_dst', 'type':'uint32'},
				]},
			]},
			{'name':'instructions', 'fields':[
				##TODO: This Handling is bad
				{'name':'element', 'type':'TLV', 'fields':[
					{'name':'table_id', 'type':'uint48'},
				]},
			]},
			{'name':'actions', 'fields':[
				##TODO: This Handling is bad
				{'name':'element', 'type':'TLV', 'fields':[
					{'name':'port', 'type':'port'}, #uint32
					{'name':'max_len', 'type':'uint16'},
				]},
			]},
		]},
	]},
]

fields_of_flow_stats_request = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'flags', 'type':'uint16'},
	{'name':'table_id', 'type':'uint8'},
	{'name':'out_port', 'type':'uint16'},
	{'name':'out_group', 'type':'uint16'},
	{'name':'cookie', 'type':'uint32'},
	{'name':'cookie_mask', 'type':'uint32'},
	{'name':'match', 'fields': [
		{'name':'version', 'type':'uint8'},
		{'name':'fields', 'fields':[
			{'name':'in_port', 'type':'port'}, #uint32
			{'name':'in_phy_port', 'type':'port'}, #uint32
			{'name':'metadata', 'type':'uint64'},
			{'name':'eth_dst', 'type':'uint48'},
			{'name':'eth_src', 'type':'uint48'},
			{'name':'eth_type', 'type':'uint16'},
			{'name':'vlan_vid', 'type':'uint16'},
			{'name':'vlan_pcp', 'type':'uint8'},
			{'name':'ip_dscp', 'type':'uint8'},
			{'name':'ip_ecn', 'type':'uint8'},
			{'name':'ip_proto', 'type':'uint8'},
			{'name':'ipv4_src', 'type':'uint32'},
			{'name':'ipv4_dst', 'type':'uint32'},
			{'name':'tcp_src', 'type':'uint16'},
			{'name':'tcp_dst', 'type':'uint16'},
			{'name':'udp_src', 'type':'uint16'},
			{'name':'udp_dst', 'type':'uint16'},
			{'name':'sctp_src', 'type':'uint16'},
			{'name':'sctp_dst', 'type':'uint16'},
			{'name':'icmpv4_type', 'type':'uint8'},
			{'name':'icmpv4_code', 'type':'uint8'},
			{'name':'arp_op', 'type':'uint16'},
			{'name':'arp_spa', 'type':'uint32'},
			{'name':'arp_tpa', 'type':'uint32'},
			{'name':'arp_sha', 'type':'uint48'},
			{'name':'arp_tha', 'type':'uint48'},
			{'name':'ipv6_src', 'impl':False, 'type':'uint128'},
			{'name':'ipv6_dst', 'impl':False, 'type':'uint128'},
			{'name':'ipv6_flabel', 'type':'uint32'},
			{'name':'icmpv6_type', 'type':'uint8'},
			{'name':'icmpv6_code', 'type':'uint8'},
			{'name':'ipv6_nd_target', 'impl':False, 'type':'uint128'},
			{'name':'ipv6_nd_sll', 'type':'uint48'},
			{'name':'ipv6_nd_tll', 'type':'uint48'},
			{'name':'mpls_label', 'type':'uint32'},
			{'name':'mpls_tc', 'type':'uint8'},
			{'name':'mpls_bos', 'type':'uint8'},
			{'name':'tunnel_id', 'type':'uint64'},
			{'name':'ipv6_exthdr', 'type':'uint16'},
			{'name':'pbb_uca', 'type':'uint8'},
			{'name':'tunnel_ipv4_src', 'type':'uint32'},
			{'name':'tunnel_ipv4_dst', 'type':'uint32'},
		]},
		{'name':'masks', 'fields':[
			{'name':'in_port', 'type':'uint32'},
			{'name':'in_phy_port', 'type':'uint32'},
			{'name':'metadata', 'type':'uint64'},
			{'name':'eth_dst', 'type':'uint48'},
			{'name':'eth_src', 'type':'uint48'},
			{'name':'eth_type', 'type':'uint16'},
			{'name':'vlan_vid', 'type':'uint16'},
			{'name':'vlan_pcp', 'type':'uint8'},
			{'name':'ip_dscp', 'type':'uint8'},
			{'name':'ip_ecn', 'type':'uint8'},
			{'name':'ip_proto', 'type':'uint8'},
			{'name':'ipv4_src', 'type':'uint32'},
			{'name':'ipv4_dst', 'type':'uint32'},
			{'name':'tcp_src', 'type':'uint16'},
			{'name':'tcp_dst', 'type':'uint16'},
			{'name':'udp_src', 'type':'uint16'},
			{'name':'udp_dst', 'type':'uint16'},
			{'name':'sctp_src', 'type':'uint16'},
			{'name':'sctp_dst', 'type':'uint16'},
			{'name':'icmpv4_type', 'type':'uint8'},
			{'name':'icmpv4_code', 'type':'uint8'},
			{'name':'arp_op', 'type':'uint16'},
			{'name':'arp_spa', 'type':'uint32'},
			{'name':'arp_tpa', 'type':'uint32'},
			{'name':'arp_sha', 'type':'uint48'},
			{'name':'arp_tha', 'type':'uint48'},
			{'name':'ipv6_src', 'impl':False, 'type':'uint128'},
			{'name':'ipv6_dst', 'impl':False, 'type':'uint128'},
			{'name':'ipv6_flabel', 'type':'uint32'},
			{'name':'icmpv6_type', 'type':'uint8'},
			{'name':'icmpv6_code', 'type':'uint8'},
			{'name':'ipv6_nd_target', 'impl':False, 'type':'uint128'},
			{'name':'ipv6_nd_sll', 'type':'uint48'},
			{'name':'ipv6_nd_tll', 'type':'uint48'},
			{'name':'mpls_label', 'type':'uint32'},
			{'name':'mpls_tc', 'type':'uint8'},
			{'name':'mpls_bos', 'type':'uint8'},
			{'name':'tunnel_id', 'type':'uint64'},
			{'name':'ipv6_exthdr', 'type':'uint16'},
			{'name':'pbb_uca', 'type':'uint8'},
			{'name':'tunnel_ipv4_src', 'type':'uint32'},
			{'name':'tunnel_ipv4_dst', 'type':'uint32'},
		]},
	]},
]

fields_of_get_config_reply = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'flags', 'type':'uint16'},
	{'name':'miss_send_len', 'type':'uint16'},
]

fields_of_get_config_request = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
]

fields_of_group_add = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'flags', 'type':'uint16'},
	{'name':'group_type', 'type':'uint8'},
	{'name':'group_id', 'type':'uint32'},
	{'name':'buckets','fields':[
		{'name':'element','type':'list', 'fields':[
			{'name':'weight', 'type':'uint16'},
			{'name':'watch_port', 'type':'port'}, #uint32
			{'name':'watch_group', 'type':'uint32'},
			{'name':'actions','fields':[
				##TODO: This Handling is bad
				{'name':'element','type':'TLV', 'fields': [
					{'name':'port', 'type':'port'}, #uint32
					{'name':'max_len', 'type':'uint16'},
				]},
			]},
		]},
	]},
]

fields_of_group_delete = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'flags', 'type':'uint16'},
	{'name':'group_type', 'type':'uint8'},
	{'name':'group_id', 'type':'uint32'},
	{'name':'buckets','fields':[
		{'name':'element','type':'list', 'fields':[
			{'name':'weight', 'type':'uint16'},
			{'name':'watch_port', 'type':'port'}, #uint32
			{'name':'watch_group', 'type':'uint32'},
			{'name':'actions','fields':[
				##TODO: This Handling is bad
				{'name':'element','type':'TLV', 'fields': [
					{'name':'port', 'type':'port'}, #uint32
					{'name':'max_len', 'type':'uint16'},
				]},
			]},
		]},
	]},
]

fields_of_group_desc_stats_reply = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'flags', 'type':'uint16'},
	{'name':'entries', 'fields':[
		{'name':'element','type':'list', 'fields':[
			{'name':'group_type', 'type':'uint8'},
			{'name':'group_id', 'type':'uint32'},
			{'name':'buckets','fields':[
				{'name':'element','type':'list', 'fields':[
					{'name':'weight', 'type':'uint16'},
					{'name':'watch_port', 'type':'port'}, #uint32
					{'name':'watch_group', 'type':'uint32'},
					{'name':'actions','fields':[
						##TODO: This Handling is bad
						{'name':'element','type':'TLV', 'fields': [
							{'name':'port', 'type':'port'}, #uint32
							{'name':'max_len', 'type':'uint16'},
						]},
					]},
				]},
			]},
		]},
	]},
]

fields_of_group_desc_stats_request = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'flags', 'type':'uint16'},
]

fields_of_group_features_stats_reply = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'flags', 'type':'uint16'},
	{'name':'types', 'type':'uint32'},
	{'name':'max_groups_all', 'type':'uint32'},
	{'name':'max_groups_select', 'type':'uint32'},
	{'name':'max_groups_indrect', 'type':'uint32'},
	{'name':'max_groups_ff', 'type':'uint32'},
	{'name':'actions_all', 'type':'uint32'},
	{'name':'actions_select', 'type':'uint32'},
	{'name':'actions_indirect', 'type':'uint32'},
	{'name':'actions_ff', 'type':'uint32'},
]

fields_of_group_features_stats_request = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'flags', 'type':'uint16'},
]

fields_of_group_mod_failed_error_msg = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'code', 'type':'uint16'},
	{'name':'data', 'impl':False},
]

fields_of_group_modify = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'flags', 'type':'uint16'},
	{'name':'group_type', 'type':'uint8'},
	{'name':'group_id', 'type':'uint32'},
	{'name':'buckets','fields':[
		{'name':'element','type':'list', 'fields':[
			{'name':'weight', 'type':'uint16'},
			{'name':'watch_port', 'type':'port'}, #uint32
			{'name':'watch_group', 'type':'uint32'},
			{'name':'actions','fields':[
				##TODO: This Handling is bad
				{'name':'element','type':'TLV', 'fields': [
					{'name':'port', 'type':'port'}, #uint32
					{'name':'max_len', 'type':'uint16'},
				]},
			]},
		]},
	]},
]

fields_of_group_stats_reply = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'flags', 'type':'uint16'},
	{'name':'entries', 'fields':[
		{'name':'element','type':'list', 'fields':[
			{'name':'group_id', 'type':'uint32'},
			{'name':'ref_count', 'type':'uint32'},
			{'name':'packet_count', 'type':'uint64'},
			{'name':'byte_count', 'type':'uint64'},
			{'name':'duration_sec', 'type':'uint32'},
			{'name':'duration_nsec', 'type':'uint32'},
			{'name':'bucket_stats', 'fields':[
				{'name':'element','type':'list', 'fields':[
					{'name':'packet_count', 'type':'uint64'},
					{'name':'byte_count', 'type':'uint64'},
				]},
			]},
		]},
	]},
]

fields_of_group_stats_request = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'flags', 'type':'uint16'},
	{'name':'group_id', 'type':'uint32'},
]

fields_of_hello = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'elements','type':'list', 'fields':[
		{'name':'element','type':'list', 'max':1, 'fields':[
			{'name':'version_bitmap', 'fields':[
				{'name':'element','type':'list', 'max':1, 'fields':[
					{'name':'uint32', 'type':'uint32'},
				]},
			]},
		]},
	]},
]

fields_of_hello_failed_error_msg = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'code', 'type':'uint16'},
	{'name':'data', 'impl':False},
]

fields_of_meter_config_stats_reply = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'flags', 'type':'uint16'},
	{'name':'entries', 'fields':[
		{'name':'element','type':'list','fields':[
			{'name':'flags', 'type':'uint16'},
			{'name':'meter_id', 'type':'uint32'},
			{'name':'entries', 'fields':[
				##TODO: This Handling is bad
				{'name':'element','type':'TLV','fields':[
					{'name':'rate', 'type':'uint32'},
					{'name':'burst_size', 'type':'uint32'},
					{'name':'prec_level', 'type':'uint8'},
				]},
			]},
		]},
	]},
]

fields_of_meter_config_stats_request = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'flags', 'type':'uint16'},
	{'name':'meter_id', 'type':'uint32'},
]

fields_of_meter_features_stats_reply = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'flags', 'type':'uint16'},
	{'name':'features', 'fields':[
		{'name':'max_meter', 'type':'uint32'},
		{'name':'band_types', 'type':'uint32'},
		{'name':'capabilities', 'type':'uint32'},
		{'name':'max_bands', 'type':'uint8'},
		{'name':'max_color', 'type':'uint8'},
	]},
]

fields_of_meter_features_stats_request = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'flags', 'type':'uint16'},
]

fields_of_meter_mod = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'flags', 'type':'uint16'},
	{'name':'meter_id', 'type':'uint32'},
	{'name':'bands', 'fields':[
		##TODO: This Handling is bad
		{'name':'element','type':'TLV','fields':[
			{'name':'rate', 'type':'uint32'},
			{'name':'burst_size', 'type':'uint32'},
			{'name':'prec_level', 'type':'uint8'},
		]},
	]},
	{'name':'meters', 'fields':[
		##TODO: This Handling is bad
		{'name':'element','type':'TLV','fields':[
			{'name':'rate', 'type':'uint32'},
			{'name':'burst_size', 'type':'uint32'},
			{'name':'prec_level', 'type':'uint8'},
		]},
	]},
]

fields_of_meter_mod_failed_error_msg = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'code', 'type':'uint16'},
	{'name':'data', 'impl':False},
]

fields_of_meter_stats_reply = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'entries', 'fields':[
		{'name':'element','type':'list','fields':[
			{'name':'meter_id', 'type':'uint32'},
			{'name':'flow_count', 'type':'uint32'},
			{'name':'packet_in_count', 'type':'uint64'},
			{'name':'byte_in_count', 'type':'uint64'},
			{'name':'duration_sec', 'type':'uint32'},
			{'name':'duration_nsec', 'type':'uint32'},
			{'name':'band_stats', 'fields':[
				{'name':'element','type':'list','fields':[
					{'name':'packet_count', 'type':'uint64'},
					{'name':'byte_count', 'type':'uint64'},
				]},
			]},
		]},
	]},
]

fields_of_meter_stats_request = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'flags', 'type':'uint16'},
	{'name':'meter_id', 'type':'uint32'},
]

fields_of_packet_in = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'buffer_id', 'type':'uint32'},
	{'name':'total_len', 'type':'uint16'},
	{'name':'reason', 'type':'uint8'},
	{'name':'table_id', 'type':'uint8'},
	{'name':'cookie', 'type':'uint64'},
	{'name':'match', 'fields': [
		{'name':'version', 'type':'uint8'},
		{'name':'fields', 'fields':[
			{'name':'in_port', 'type':'port'}, #uint32
			{'name':'in_phy_port', 'type':'port'}, #uint32
			{'name':'metadata', 'type':'uint64'},
			{'name':'eth_dst', 'type':'uint48'},
			{'name':'eth_src', 'type':'uint48'},
			{'name':'eth_type', 'type':'uint16'},
			{'name':'vlan_vid', 'type':'uint16'},
			{'name':'vlan_pcp', 'type':'uint8'},
			{'name':'ip_dscp', 'type':'uint8'},
			{'name':'ip_ecn', 'type':'uint8'},
			{'name':'ip_proto', 'type':'uint8'},
			{'name':'ipv4_src', 'type':'uint32'},
			{'name':'ipv4_dst', 'type':'uint32'},
			{'name':'tcp_src', 'type':'uint16'},
			{'name':'tcp_dst', 'type':'uint16'},
			{'name':'udp_src', 'type':'uint16'},
			{'name':'udp_dst', 'type':'uint16'},
			{'name':'sctp_src', 'type':'uint16'},
			{'name':'sctp_dst', 'type':'uint16'},
			{'name':'icmpv4_type', 'type':'uint8'},
			{'name':'icmpv4_code', 'type':'uint8'},
			{'name':'arp_op', 'type':'uint16'},
			{'name':'arp_spa', 'type':'uint32'},
			{'name':'arp_tpa', 'type':'uint32'},
			{'name':'arp_sha', 'type':'uint48'},
			{'name':'arp_tha', 'type':'uint48'},
			{'name':'ipv6_src', 'impl':False, 'type':'uint128'},
			{'name':'ipv6_dst', 'impl':False, 'type':'uint128'},
			{'name':'ipv6_flabel', 'type':'uint32'},
			{'name':'icmpv6_type', 'type':'uint8'},
			{'name':'icmpv6_code', 'type':'uint8'},
			{'name':'ipv6_nd_target', 'impl':False, 'type':'uint128'},
			{'name':'ipv6_nd_sll', 'type':'uint48'},
			{'name':'ipv6_nd_tll', 'type':'uint48'},
			{'name':'mpls_label', 'type':'uint32'},
			{'name':'mpls_tc', 'type':'uint8'},
			{'name':'mpls_bos', 'type':'uint8'},
			{'name':'tunnel_id', 'type':'uint64'},
			{'name':'ipv6_exthdr', 'type':'uint16'},
			{'name':'pbb_uca', 'type':'uint8'},
			{'name':'tunnel_ipv4_src', 'type':'uint32'},
			{'name':'tunnel_ipv4_dst', 'type':'uint32'},
		]},
		{'name':'masks', 'fields':[
			{'name':'in_port', 'type':'uint32'},
			{'name':'in_phy_port', 'type':'uint32'},
			{'name':'metadata', 'type':'uint64'},
			{'name':'eth_dst', 'type':'uint48'},
			{'name':'eth_src', 'type':'uint48'},
			{'name':'eth_type', 'type':'uint16'},
			{'name':'vlan_vid', 'type':'uint16'},
			{'name':'vlan_pcp', 'type':'uint8'},
			{'name':'ip_dscp', 'type':'uint8'},
			{'name':'ip_ecn', 'type':'uint8'},
			{'name':'ip_proto', 'type':'uint8'},
			{'name':'ipv4_src', 'type':'uint32'},
			{'name':'ipv4_dst', 'type':'uint32'},
			{'name':'tcp_src', 'type':'uint16'},
			{'name':'tcp_dst', 'type':'uint16'},
			{'name':'udp_src', 'type':'uint16'},
			{'name':'udp_dst', 'type':'uint16'},
			{'name':'sctp_src', 'type':'uint16'},
			{'name':'sctp_dst', 'type':'uint16'},
			{'name':'icmpv4_type', 'type':'uint8'},
			{'name':'icmpv4_code', 'type':'uint8'},
			{'name':'arp_op', 'type':'uint16'},
			{'name':'arp_spa', 'type':'uint32'},
			{'name':'arp_tpa', 'type':'uint32'},
			{'name':'arp_sha', 'type':'uint48'},
			{'name':'arp_tha', 'type':'uint48'},
			{'name':'ipv6_src', 'impl':False, 'type':'uint128'},
			{'name':'ipv6_dst', 'impl':False, 'type':'uint128'},
			{'name':'ipv6_flabel', 'type':'uint32'},
			{'name':'icmpv6_type', 'type':'uint8'},
			{'name':'icmpv6_code', 'type':'uint8'},
			{'name':'ipv6_nd_target', 'impl':False, 'type':'uint128'},
			{'name':'ipv6_nd_sll', 'type':'uint48'},
			{'name':'ipv6_nd_tll', 'type':'uint48'},
			{'name':'mpls_label', 'type':'uint32'},
			{'name':'mpls_tc', 'type':'uint8'},
			{'name':'mpls_bos', 'type':'uint8'},
			{'name':'tunnel_id', 'type':'uint64'},
			{'name':'ipv6_exthdr', 'type':'uint16'},
			{'name':'pbb_uca', 'type':'uint8'},
			{'name':'tunnel_ipv4_src', 'type':'uint32'},
			{'name':'tunnel_ipv4_dst', 'type':'uint32'},
		]},
	]},
	{'name':'data', 'impl':False},
	{'name':'in_port', 'type':'port'}, #uint32
	{'name':'in_phy_port', 'type':'port'}, #uint32
]

fields_of_packet_out = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'buffer_id', 'type':'uint32'},
	{'name':'in_port', 'type':'uint32'},
	{'name':'actions','fields':[
		##TODO: This Handling is bad
		{'name':'element','type':'TLV', 'fields': [
			{'name':'port', 'type':'port'}, #uint32
			{'name':'max_len', 'type':'uint16'},
		]},
	]},
	{'name':'data', 'impl':False},
]

fields_of_port_desc_stats_reply = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'flags', 'type':'uint16'},
	{'name':'entries', 'fields':[
		{'name':'element','type':'list', 'fields':[
			{'name':'port_no', 'type':'port'}, #uint32
			{'name':'hw_addr', 'type':'uint48'},
			{'name':'name', 'impl':False},
			{'name':'config', 'type':'uint32'},
			{'name':'state', 'type':'uint32'},
			{'name':'properties', 'fields':[
				##TODO: This Handling is bad
				{'name':'element','type':'TLV', 'max':3, 'fields':[
					{'name':'curr', 'type':'uint32'},
					{'name':'advertised', 'type':'uint32'},
					{'name':'supported', 'type':'uint32'},
					{'name':'peer', 'type':'uint32'},
					{'name':'curr_speed', 'type':'uint32'},
					{'name':'max_speed', 'type':'uint32'},
					{'name':'rx_grid_freq_lmda', 'type':'uint32'},
					{'name':'tx_pwr_min', 'type':'uint32'},
					{'name':'tx_pwr_max', 'type':'uint32'},
				]},
			]},
			{'name':'curr', 'type':'uint32'},
			{'name':'advertised', 'type':'uint32'},
			{'name':'supported', 'type':'uint32'},
			{'name':'peer', 'type':'uint32'},
			{'name':'curr_speed', 'type':'uint32'},
			{'name':'max_speed', 'type':'uint32'},
		]},
	]}
]

fields_of_port_desc_stats_request = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'flags', 'type':'uint16'},
]

fields_of_port_mod = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'port_no', 'type':'port'}, #uint32
	{'name':'hw_addr', 'impl':False},
	{'name':'config', 'type':'uint32'},
	{'name':'mask', 'type':'uint32'},
	{'name':'properties', 'fields':[
		##TODO: This Handling is bad
		{'name':'element','type':'TLV', 'max':1, 'fields':[
			{'name':'advertise', 'type':'uint32'},
			{'name':'freq_ldma', 'type':'uint32'},
			{'name':'fl_offset', 'type':'uint32'},
			{'name':'grid_span', 'type':'uint32'},
			{'name':'tx_pwr', 'type':'uint32'},
		]},
	]},
	{'name':'advertise', 'type':'uint32'},
]

fields_of_port_mod_failed_error_msg = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'code', 'type':'uint16'},
	{'name':'data', 'impl':False},
]

fields_of_port_stats_reply = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'flags', 'type':'uint16'},
	{'name':'entries', 'fields':[
		{'name':'element','type':'list', 'fields':[
			{'name':'port_no', 'type':'port'}, #uint32
			{'name':'duration_sec', 'type':'uint32'},
			{'name':'duration_nsec', 'type':'uint32'},
			{'name':'rx_packets', 'type':'uint64'},
			{'name':'tx_packets', 'type':'uint64'},
			{'name':'rx_bytes', 'type':'uint64'},
			{'name':'tx_bytes', 'type':'uint64'},
			{'name':'rx_dropped', 'type':'uint64'},
			{'name':'tx_dropped', 'type':'uint64'},
			{'name':'rx_errors', 'type':'uint64'},
			{'name':'tx_errors', 'type':'uint64'},
			{'name':'properties', 'fields':[
				##TODO: This Handling is bad
				{'name':'element','type':'TLV', 'max':3, 'fields':[
					{'name':'rx_frame_err', 'type':'uint64'},
					{'name':'rx_over_err', 'type':'uint64'},
					{'name':'rx_crc_err', 'type':'uint64'},
					{'name':'collisions', 'type':'uint64'},
					{'name':'rx_freq_lmda', 'type':'uint32'},
					{'name':'rx_offset', 'type':'uint32'},
					{'name':'rx_grid_span', 'type':'uint32'},
					{'name':'tx_pwr', 'type':'uint16'},
					{'name':'rx_pwr', 'type':'uint16'},
					{'name':'bias_current', 'type':'uint16'},
					{'name':'temperature', 'type':'uint16'},
				]},
			]},
			{'name':'rx_frame_err', 'type':'uint64'},
			{'name':'rx_over_err', 'type':'uint64'},
			{'name':'rx_crc_err', 'type':'uint64'},
			{'name':'collisions', 'type':'uint64'},
		]},
	]}
]

fields_of_port_stats_request = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'flags', 'type':'uint16'},
	{'name':'port_no', 'type':'port'}, #uint32
]

fields_of_port_status = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'reason', 'type':'uint8'},
	{'name':'desc', 'fields':[
		{'name':'port_no', 'type':'port'}, #uint32
		{'name':'hw_addr', 'type':'uint48'},
		{'name':'name', 'impl':False},
		{'name':'config', 'type':'uint32'},
		{'name':'state', 'type':'uint32'},
		{'name':'properties', 'fields':[
			##TODO: This Handling is bad
			{'name':'element','type':'TLV', 'max':3, 'fields':[
				{'name':'curr', 'type':'uint32'},
				{'name':'advertised', 'type':'uint32'},
				{'name':'supported', 'type':'uint32'},
				{'name':'peer', 'type':'uint32'},
				{'name':'curr_speed', 'type':'uint32'},
				{'name':'max_speed', 'type':'uint32'},
				{'name':'rx_grid_freq_lmda', 'type':'uint32'},
				{'name':'tx_pwr_min', 'type':'uint32'},
				{'name':'tx_pwr_max', 'type':'uint32'},
			]},
		]},
		{'name':'curr', 'type':'uint32'},
		{'name':'advertised', 'type':'uint32'},
		{'name':'supported', 'type':'uint32'},
		{'name':'peer', 'type':'uint32'},
		{'name':'curr_speed', 'type':'uint32'},
		{'name':'max_speed', 'type':'uint32'},
	]},
]

fields_of_queue_desc_stats_reply = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'flags', 'type':'uint16'},
	{'name':'entries', 'fields':[
		{'name':'element','type':'list', 'fields':[
			{'name':'port_no', 'type':'port'}, #uint32
			{'name':'queue_id', 'type':'uint32'},
			{'name':'properties', 'fields':[
				##TODO: This Handling is bad
				{'name':'element','type':'TLV', 'max':2, 'fields':[
					{'name':'rate', 'type':'uint16'},
				]},
			]},
		]},
	]},
]

fields_of_queue_desc_stats_request = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'flags', 'type':'uint16'},
]

fields_of_queue_get_config_reply = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'port', 'type':'port'}, #uint32
	{'name':'queues', 'fields':[
		{'name':'element','type':'list', 'fields':[
			{'name':'queue_id', 'type':'uint32'},
			{'name':'port', 'type':'port'}, #uint32
			{'name':'properties', 'fields':[
				##TODO: This Handling is bad
				{'name':'element','type':'TLV', 'max':2, 'fields':[
					{'name':'rate', 'type':'uint16'},
				]},
			]},
		]},
	]},
]

fields_of_queue_get_config_request = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'port', 'type':'port'}, #uint32
]

fields_of_queue_op_failed_error_msg = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'code', 'type':'uint16'},
	{'name':'data', 'impl':False},
]

fields_of_queue_stats_reply = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'flags', 'type':'uint16'},
	{'name':'entries', 'fields':[
		{'name':'element','type':'list', 'fields':[
			{'name':'port_no', 'type':'port'}, #uint32
			{'name':'queue_id', 'type':'uint32'},
			{'name':'tx_bytes', 'type':'uint64'},
			{'name':'tx_packets', 'type':'uint64'},
			{'name':'tx_errors', 'type':'uint64'},
			{'name':'duration_sec', 'type':'uint32'},
			{'name':'duration_nsec', 'type':'uint32'},
			{'name':'properties','impl':False,'fields':[
				##TODO: This Handling is bad
				{'name':'element','type':'TLV', 'fields':[
				]},
			]},
		]},
	]},
]

fields_of_queue_stats_request = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'flags', 'type':'uint16'},
	{'name':'port_no', 'type':'port'}, #uint32
	{'name':'queue_id', 'type':'uint32'},
]

fields_of_requestforward = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'role', 'type':'uint32'},
	{'name':'data', 'impl':False},
]

fields_of_role_reply = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'role', 'type':'uint32'},
	{'name':'generation_id', 'type':'uint64'},
]

fields_of_role_request = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'role', 'type':'uint32'},
	{'name':'generation_id', 'type':'uint64'},
]

fields_of_role_request_failed_error_msg = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'code', 'type':'uint16'},
	{'name':'data', 'impl':False},
]

fields_of_role_status = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'role', 'type':'uint32'},
	{'name':'generation_id', 'type':'uint64'},
	{'name':'properties','impl':False,'fields':[
		##TODO: This Handling is bad
		{'name':'element','type':'TLV', 'fields':[
		]},
	]},
]

fields_of_set_config = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'flags', 'type':'uint16'},
	{'name':'miss_send_len', 'type':'uint16'},
]

fields_of_switch_config_failed_error_msg = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'code', 'type':'uint16'},
	{'name':'data', 'impl':False},
]

fields_of_table_desc_stats_reply = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'flags', 'type':'uint16'},
	{'name':'entries', 'fields':[
		{'name':'element','type':'list', 'fields':[
			{'name':'table_id', 'type':'uint8'},
			{'name':'config', 'type':'uint32'},
		]},
	]},
]

fields_of_table_desc_stats_request = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'flags', 'type':'uint16'},
]

fields_of_table_features_failed_error_msg = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'code', 'type':'uint16'},
	{'name':'data', 'impl':False},
]

fields_of_table_features_stats_reply = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'flags', 'type':'uint16'},
	{'name':'entries', 'fields':[
		{'name':'element','type':'list', 'fields':[
			{'name':'table_id', 'type':'uint8'},
			{'name':'name', 'impl':False},
			{'name':'metadata_match', 'type':'uint64'},
			{'name':'matadata_write', 'type':'uint64'},
			{'name':'config', 'type':'uint32'},
			{'name':'max_entries', 'type':'uint32'},
			{'name':'properties','impl':False,'fields':[
				##TODO: This Handling is bad
				{'name':'element','type':'TLV', 'max':14,'fields':[
					{'name':'ids','impl':False,'fields':[
						##TODO: This Handling is bad
						{'name':'element','type':'TLV', 'fields':[
							{'name':'field', 'type':'uint32'},
						]},
					]},
				]},
			]},
		]},
	]},
]

fields_of_table_features_stats_request = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'flags', 'type':'uint16'},
	{'name':'entries', 'fields':[
		{'name':'element','type':'list', 'fields':[
			{'name':'table_id', 'type':'uint8'},
			{'name':'name', 'impl':False},
			{'name':'metadata_match', 'type':'uint64'},
			{'name':'matadata_write', 'type':'uint64'},
			{'name':'config', 'type':'uint32'},
			{'name':'max_entries', 'type':'uint32'},
			{'name':'properties','impl':False,'fields':[
				##TODO: This Handling is bad
				{'name':'element','type':'TLV', 'max':14,'fields':[
					{'name':'ids','impl':False,'fields':[
						##TODO: This Handling is bad
						{'name':'element','type':'TLV', 'fields':[
							{'name':'field', 'type':'uint32'},
						]},
					]},
				]},
			]},
		]},
	]},
]

fields_of_table_mod = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'table_id', 'type':'uint8'},
	{'name':'config', 'type':'uint32'},
	{'name':'properties','fields':[
		##TODO: This Handling is bad
		{'name':'element','type':'TLV', 'max':2,'fields':[
			{'name':'vancancy_down', 'type':'uint8'},
			{'name':'vancancy_up', 'type':'uint8'},
			{'name':'vancancy_get', 'type':'uint8'},
		]},
	]},
]

fields_of_table_mod_failed_error_msg = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'code', 'type':'uint16'},
	{'name':'data', 'impl':False},
]

fields_of_table_stats_reply = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'flags', 'type':'uint16'},
	{'name':'entries', 'fields':[
		{'name':'element','type':'list', 'fields':[
			{'name':'table_id', 'type':'uint8'},
			{'name':'active_count', 'type':'uint32'},
			{'name':'lookup_count', 'type':'uint64'},
			{'name':'matched_count', 'type':'uint64'},
			{'name':'name', 'impl':False},
			{'name':'match', 'type':'uint64'},
			{'name':'wildcards', 'type':'uint64'},
			{'name':'write_actions', 'type':'uint32'},
			{'name':'apply_actions', 'type':'uint32'},
			{'name':'write_setfields', 'type':'uint64'},
			{'name':'apply_setfields', 'type':'uint64'},
			{'name':'metadata_match', 'type':'uint64'},
			{'name':'metadata_write', 'type':'uint64'},
			{'name':'instructions', 'type':'uint32'},
			{'name':'config', 'type':'uint32'},
			{'name':'max_entries', 'type':'uint32'},
		]},
	]},
]

fields_of_table_stats_request = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'flags', 'type':'uint16'},
]

fields_of_table_status = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'role', 'type':'uint32'},
	{'name':'reason', 'type':'uint8'},
	{'name':'table', 'type':'uint8'},
]

fields_of_nicira_controller_role_reply = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'experimenter', 'type':'uint32'},
	{'name':'subtype', 'type':'uint32'},
	{'name':'role', 'type':'uint32'},
]

fields_of_nicira_controller_role_request = [
	{'name':'version', 'type':'uint8'},
	{'name':'type', 'type':'uint8'},
	{'name':'length', 'type':'uint16'},
	{'name':'xid', 'type':'uint32'},
	{'name':'experimenter', 'type':'uint32'},
	{'name':'subtype', 'type':'uint32'},
	{'name':'role', 'type':'uint32'},
]

openflow = [
	['of_aggregate_stats_reply', fields_of_aggregate_stats_reply],
	['of_aggregate_stats_request', fields_of_aggregate_stats_request],
	['of_async_config_failed_error_msg', fields_of_async_get_reply],
	['of_async_get_reply', fields_of_async_get_reply],
	['of_async_get_request', fields_of_async_get_request],
	['of_async_set', fields_of_async_set],
	['of_bad_action_error_msg', fields_of_bad_action_error_msg],
	['of_bad_instruction_error_msg', fields_of_bad_instruction_error_msg],
	['of_bad_match_error_msg', fields_of_bad_match_error_msg],
	['of_bad_property_error_msg', fields_of_bad_property_error_msg],
	['of_bad_request_error_msg', fields_of_bad_request_error_msg],
	['of_barrier_reply', fields_of_barrier_reply],
	['of_barrier_request', fields_of_barrier_request],
	['of_bundle_add_msg', fields_of_bundle_add_msg],
	['of_bundle_ctrl_msg', fields_of_bundle_ctrl_msg],
	['of_bundle_failed_error_msg', fields_of_bundle_failed_error_msg],
	['of_desc_stats_reply', fields_of_desc_stats_reply],
	['of_desc_stats_request', fields_of_desc_stats_request],
	['of_echo_reply', fields_of_echo_reply],
	['of_echo_request', fields_of_echo_request],
	['of_experimenter', fields_of_experimenter],
	['of_experimenter_error_msg', fields_of_experimenter_error_msg],
	['of_experimenter_stats_reply', fields_of_experimenter_stats_reply],
	['of_experimenter_stats_request', fields_of_experimenter_stats_request],
	['of_features_reply', fields_of_features_reply],
	['of_features_request', fields_of_features_request],
	['of_flow_add', fields_of_flow_add],
	['of_flow_delete', fields_of_flow_delete],
	['of_flow_delete_strict', fields_of_flow_delete_strict],
	['of_flow_mod_failed_error_msg', fields_of_flow_mod_failed_error_msg],
	['of_flow_modify', fields_of_flow_modify],
	['of_flow_modify_strict', fields_of_flow_modify_strict],
	['of_flow_monitor_failed_error_msg', fields_of_flow_monitor_failed_error_msg],
	['of_flow_removed', fields_of_flow_removed],
	['of_flow_stats_reply', fields_of_flow_stats_reply],
	['of_flow_stats_request', fields_of_flow_stats_request],
	['of_get_config_reply', fields_of_get_config_reply],
	['of_get_config_request', fields_of_get_config_request],
	['of_group_add', fields_of_group_add],
	['of_group_delete', fields_of_group_delete],
	['of_group_desc_stats_reply', fields_of_group_desc_stats_reply],
	['of_group_desc_stats_request', fields_of_group_desc_stats_request],
	['of_group_features_stats_reply', fields_of_group_features_stats_reply],
	['of_group_features_stats_request', fields_of_group_features_stats_request],
	['of_group_mod_failed_error_msg', fields_of_group_mod_failed_error_msg],
	['of_group_modify', fields_of_group_modify],
	['of_group_stats_reply', fields_of_group_stats_reply],
	['of_group_stats_request', fields_of_group_stats_request],
	['of_hello', fields_of_hello],
	['of_hello_failed_error_msg', fields_of_hello_failed_error_msg],
	['of_meter_config_stats_reply', fields_of_meter_config_stats_reply],
	['of_meter_config_stats_request', fields_of_meter_config_stats_request],
	['of_meter_features_stats_reply', fields_of_meter_features_stats_reply],
	['of_meter_features_stats_request', fields_of_meter_features_stats_request],
	['of_meter_mod', fields_of_meter_mod],
	['of_meter_mod_failed_error_msg', fields_of_meter_mod_failed_error_msg],
	['of_meter_stats_reply', fields_of_meter_stats_reply],
	['of_meter_stats_request', fields_of_meter_stats_request],
	['of_packet_in', fields_of_packet_in],
	['of_packet_out', fields_of_packet_out],
	['of_port_desc_stats_reply', fields_of_port_desc_stats_reply],
	['of_port_desc_stats_request', fields_of_port_desc_stats_request],
	['of_port_mod', fields_of_port_mod],
	['of_port_mod_failed_error_msg', fields_of_port_mod_failed_error_msg],
	['of_port_stats_reply', fields_of_port_stats_reply],
	['of_port_stats_request', fields_of_port_stats_request],
	['of_port_status', fields_of_port_status],
	['of_queue_desc_stats_reply', fields_of_queue_desc_stats_reply],
	['of_queue_desc_stats_request', fields_of_queue_desc_stats_request],
	['of_queue_get_config_reply', fields_of_queue_get_config_reply],
	['of_queue_get_config_request', fields_of_queue_get_config_request],
	['of_queue_op_failed_error_msg', fields_of_queue_op_failed_error_msg],
	['of_queue_stats_reply', fields_of_queue_stats_reply],
	['of_queue_stats_request', fields_of_queue_stats_request],
	['of_requestforward', fields_of_requestforward],
	['of_role_reply', fields_of_role_reply],
	['of_role_request', fields_of_role_request],
	['of_role_request_failed_error_msg', fields_of_role_request_failed_error_msg],
	['of_role_status', fields_of_role_status],
	['of_set_config', fields_of_set_config],
	['of_switch_config_failed_error_msg', fields_of_switch_config_failed_error_msg],
	['of_table_desc_stats_reply', fields_of_table_desc_stats_reply],
	['of_table_desc_stats_request', fields_of_table_desc_stats_request],
	['of_table_features_failed_error_msg', fields_of_table_features_failed_error_msg],
	['of_table_features_stats_reply', fields_of_table_features_stats_reply],
	['of_table_features_stats_request', fields_of_table_features_stats_request],
	['of_table_mod', fields_of_table_mod],
	['of_table_mod_failed_error_msg', fields_of_table_mod_failed_error_msg],
	['of_table_stats_reply', fields_of_table_stats_reply],
	['of_table_stats_request', fields_of_table_stats_request],
	['of_table_status', fields_of_table_status],
	['of_nicira_controller_role_reply', fields_of_nicira_controller_role_reply],
	['of_nicira_controller_role_request', fields_of_nicira_controller_role_request],
]
