import pandas as pd
from src.detector_ia import detectar

def test_detector_longitud_y_binario():
    train=pd.DataFrame({'temperatura':[69,70,71,72,73,69,70,71,72,73], 'tasa_defectos':[1,2,1,2,3,2,1,3,2,1]})
    eval_df=pd.DataFrame({'temperatura':[70,120], 'tasa_defectos':[2,15]})
    pred=detectar(train,eval_df)
    assert len(pred)==2 and set(pred).issubset({0,1})
