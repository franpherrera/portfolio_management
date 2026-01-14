import pandas as pd
import yfinance as yf
from pydantic import BaseModel, field_validator,Field
from typing import Dict
"""
Creo que es buenos validar elformato de las current shares y el target allocations
Por ejemplo que los sumen 1.0 que sean decimales y que por ejemplo las acciones que tengo en mi
poder son positivas
"""
class StockFormat(BaseModel):
    target_allocations: Dict[str,float]
    shares_current: Dict[str,float]

    @field_validator("target_allocations")
    @classmethod
    def check_positive_allocations(cls,v):
        #Primero chequear si todos los targets allocations son positivos
        for i in v.values():
            if i <0:
                raise ValueError(f"Allocation vaues alues must be positive:{v}")
        return v
    
    @field_validator("target_allocations")
    @classmethod
    def sum_unit(cls,v):
        if not abs(sum(v.values()) -1.0) < 1e-6:
            raise ValueError("target allocation sum must sum 1.0")
        return v
    
    @field_validator("shares_current")
    @classmethod
    def check_positive_shares(cls,v):
        #Primero chequear si todos los targets allocations son positivos
        for i in v.values():
            if i <0:
                raise ValueError(f"shares vaues alues must be positive:{v}")
        return v


class Portfolio:
    def __init__(self, target_allocation:dict, current_shares:dict,mode=0):
        allocations=target_allocation
        shares_current=current_shares
        validate_data = StockFormat(target_allocations=allocations,shares_current=current_shares)

        
        self.target_allocation = pd.Series(target_allocation)
        self.current_shares = pd.Series(current_shares)
        self.mode = 0
        """
        Se me ocurre una flag para definir si se querie usar otro tipo de libreria para optimizar el rebalance o sugerencia de otras acciones. El modo 0 seria seria el clawsico 60/40
        -----------------------------------------------------------------------------------
         Ejemplo de formato de targt allcoations
        {"AAPL":0.60
        "META":0.4}
        Ejemlop de formato pra current_shares
        {"AAPL":1000
        "META":500}
        """
    def target_checker(self):
        pass
    def get_current_price(self):
        #Primero estoy evaluando cuales son los paramentros que entrega la API de Yfinance. Usando ejemplos de la documentacion de yfinance
        #https://ranaroussi.github.io/yfinance/
        #tickers = yf.Tickers('MSFT,AAPL,GOOG')
        #print(tickers.tickers['MSFT'].info.items())
        ticker_list ={}
        #list(map(lambda x: ticker_list.append(x),self.target_allocation))
        
        for ticker in list(self.target_allocation.keys()):
            ticker_yfinance = yf.Ticker(ticker)
            #data = ticker_yfinance.history()
            #last_price = data['Close'].iloc[-1]
            #print(ticker,last_price)
            current_price = ticker_yfinance.info['regularMarketPrice']
            #print(f"{ticker},{current_price}")
            ticker_list[ticker]=current_price
        return pd.Series(ticker_list)            

    def portfolio_value(self):
        #Que sucede si tengo una meta de nuevas share allocations de las que no tengo shares actualmente
        new_stock = self.target_allocation.index.symmetric_difference(self.current_shares.index)
        #print(new_stock)
        if new_stock.size !=0:
            self.current_shares = self.current_shares.reindex(self.target_allocation.index, fill_value=0)
        #Ver el valor total del portfolio de acuerdo al precio actual reportado por la funcion get_current_price
        current_prices = self.get_current_price()
        portfolio_value_share = current_prices*self.current_shares #Pandas series 
        total_portafolio_value = portfolio_value_share.sum()
        
        return total_portafolio_value,portfolio_value_share

    def rebalance(self):
        total_portfolio_value,portfolio_value_share= self.portfolio_value()
        
        target_values = total_portfolio_value*self.target_allocation
        
        """
        Calculo de cantidad de dolares para realizar el balance del portafolio
        Se calcula si es que existe un "drift" de acuerdo a los target allocations definidos anteteriormente
        """
        current_prices = self.get_current_price()
        delta_dollars = target_values - portfolio_value_share
        delta_shares = delta_dollars / current_prices
        #print(delta_dollars)
        #caluclar cuanto debes comprar de la nueva stock
        portfolio_proposal = {}
        for key,value in delta_shares.items():
            """
            # Si valor de delta es positivo, se tiene que comprar la cantidad de acciones de este asset
                #Si es negativo, se debe vender esta cantidad de el asset
                #0 esta joya
            """
            if value > 0:
                print(f"Se deben comprar {value} acciones de {key}")
            if value < 0 :
                print(f"Se deben vender {abs(value)} acciones de {key}")
            if value == 0:
                print(f"Nada que hacer con esa acci_on {key}")
            portfolio_proposal[key] = value    
        return pd.Series(portfolio_proposal)
                
        

        


if __name__ == "__main__":
    #allocations = {"AAPL":0.6,"META":0.4}
    allocations = {"AAPL":0.6,"META":0.2,"DLO":0.2}
    current_shares = {"AAPL":10,"META":40}
    dummy_test = Portfolio(allocations,current_shares)
    print(dummy_test.rebalance())
    
    



