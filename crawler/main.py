#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from crawler import run_crawler

stocks = ['$GOOG', '$WINS', '$GV', '$CC', '$KEM', '$CWEI', '$ZIONW', '$AMD', '$REN', '$STI.B', '$CRBP', '$EVI', '$EXEL', '$TWNKW', '$GST-B', '$LNTH', '$GST-A',
          '$AKAO', '$TROX', '$VAL.P', '$OIB.C', '$TELL', '$NRP', '$ASMB', '$GRVY', '$AAOI', '$BAC.A', '$STI.A', '$CMA.W', '$ZYNE', '$CDZI',
          '$GGB', '$LTRX', '$NBEV', '$PME', '$HSKA', '$STM', '$PCMI', '$HIIQ', '$WLDN', '$FELP', '$SHLO', '$AXTI', '$CARA', '$VEDL', '$NOA', 
          '$PNC.W', '$UCTT', '$SODA', '$LGCYO', '$WIX', '$X', '$EBR', '$CLVS', '$TSRO', '$BBGI', '$WB', '$ARRY', '$TMST', '$MTB.W', '$JPM.W', '$NVDA', '$SNOW',
          '$PLSE', '$AEHR', '$VALE', '$GOL', '$UNT', '$GKOS', '$CLCD', '$CRNT', '$CRHM', '$AAMC', '$IMMU', '$HSC', '$CVEO', '$DTRM', '$MASI', '$FMSA', '$BSBR', 
          '$YRD', '$LGCYP', '$NEFF', '$TCBI', '$HCLP', '$IVAC', '$TRUE', '$BWEN', '$STS', '$ATRS', '$SGMS', '$ZLTQ', '$CARB', '$SHOP', '$EXTN',
          '$NTRI', '$BCOR', '$OTIV', '$TTMI', '$ORN', '$NMIH']

for stock in stocks:
    run_crawler(stock, 1000)
    time.sleep(900)
    #sleeps 15 minutes
