### Imports
from sklearn.preprocessing import MinMaxScaler
import pickle as pkl
import os

class transform_data:
    
    def normalizacao( data, mms = '' ):
        data_n  = data.copy()
        arquivo = '../data/pikle/mms.sav'

        cols    = ['BALANCE', 'PURCHASES', 'ONEOFF_PURCHASES', 'INSTALLMENTS_PURCHASES', 'CASH_ADVANCE', 'CASH_ADVANCE_FREQUENCY', 'CASH_ADVANCE_TRX', 'PURCHASES_TRX', 'CREDIT_LIMIT', 'PAYMENTS', 'MINIMUM_PAYMENTS', 'TENURE']
        if mms == '':
            mms    = MinMaxScaler()
            mms = mms.fit( data_n[cols] )
            data_n[cols] = mms.transform( data_n[cols] )
            if os.path.isfile( arquivo ):
                print( 'Arquivo de normalização(MinMaxScaller) já existente' )
            else:
                pkl.dump( mms, open( '../data/pikle/mms.sav', 'wb' ) )
                
            return data_n, mms
        else:
            mms.transform( data_n[cols] ) 
            return data_n   




           

            