import pandas as pd


class KX:
    @staticmethod
    def const(kx:float, E_mod:float=1) -> float:
        return E_mod * kx

    @staticmethod
    def constRectangular(dx_glob:float, dy_glob:float, E_mod:float=1) -> float:
        return E_mod * dy_glob * dx_glob**3 / 12 #EIy
    
    @staticmethod
    def from_csv(csv_path:str, momYColName:str, EIYColName:str) -> pd.DataFrame:
        df_all = pd.read_csv(csv_path)
        df_momEIy = df_all[[momYColName, EIYColName]]
        return df_momEIy
    
    
class KY:
    @staticmethod
    def const(kx:float) -> float:
        return kx

    @staticmethod
    def constRectangular(dx_glob:float, dy_glob:float, E_mod:float=1) -> float:
        return E_mod * dx_glob * dy_glob**3 / 12 #EIx
    
    @staticmethod
    def from_csv(csv_path:str, momXColName:str, EIXColName:str) -> pd.DataFrame:
        df_all = pd.read_csv(csv_path)
        df_momEIy = df_all[[momXColName, EIXColName]]
        return df_momEIy