# ------------------------------------------------------------------------
# Copyright (c) 2020 Hangzhou Duomai E-commerce Co., Ltd.
# License: Sans, mailto:sans@duomai.com
#
# ------------------------------------------------------------------------

from duomai.duomai import *

# ------------------------------------------------------------------------------
# define the supported service
# ------------------------------------------------------------------------------
duomai.Serv.ads = SERV_ADS
duomai.Serv.link = SERV_LINKS
duomai.Serv.orders = SERV_ORDER
duomai.Serv.orderdetail = SERV_ORDER_DETAIL
duomai.Serv.settlement = SERV_ORDER_SETTLEMENT
get_ads = duomai.Serv.ads
get_link = duomai.Serv.link
get_orders = duomai.Serv.orders
get_order_detail = duomai.Serv.orderdetail
get_settlement = duomai.Serv.settlement

# ------------------------------------------------------------------------------
# include utils
# ------------------------------------------------------------------------------
duomai.parse_json = duomai.utils.parse_json
duomai.json_stringify = duomai.utils.json_stringify
duomai.md5 = duomai.utils.md5
duomai.make_query_string = duomai.utils.make_query_string
duomai.now_stamp = duomai.utils.now_stamp
