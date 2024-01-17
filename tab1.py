import streamlit as st 
# import plotly.express as px

def run_tab(): 
    # ----------------------------------------------------------------------- layout 
    t1_head0, t1_head1, t1_head2, t1_head3, t1_head4 = st.columns( [0.2, 0.2, 0.2, 0.2, 0.2] )
    
    t1_body0, t1_body1, t1_body2, t1_body3, t1_body4 = st.columns( [0.2, 0.2, 0.2, 0.2, 0.2] )

    t1_tail0, t1_tail1, t1_tail2, tail3, t1_t1_tail4 = st.columns( [0.2, 0.2, 0.2, 0.2, 0.2] )

    # -----------------------------------------------------------------------  
    t1_head0.markdown("###### 주요 민원별 현황") 
    t1_head0.markdown(r"""
	1. 현대 사회에서 부동산은 모든 사람들의 관심사항이 되었으며, 특히 서울시 소재 부동산 가격에 대한 관심은 매우 크다고 할 수 있습니다.
	2. 이번 프로젝트에서는 서울시 구별로 부동산 가격차이를 데이터 시각화를 통해 알아보고, 회귀모델을 통해 주요 원인을 찾아보고자 합니다.
    """)
    
    # -----------------------------------------------------------------------  
    t1_head1.markdown("###### 날짜") 

    # -----------------------------------------------------------------------  
    t1_head2.markdown("###### 날짜") 
    
    # -----------------------------------------------------------------------  
    t1_body0.markdown("###### 포트홀 민원") 
    t1_body0.markdown("포트홀 민원") 
    t1_body0.markdown("포트홀 민원") 
    t1_body0.markdown("포트홀 민원") 
    t1_body0.markdown("포트홀 민원") 
    t1_body0.markdown("포트홀 민원") 
    t1_body0.markdown("포트홀 민원") 
    t1_body0.markdown("포트홀 민원") 

    # -----------------------------------------------------------------------  
    t1_body1.markdown("###### 휴게소 민원") 

    # -----------------------------------------------------------------------  
    t1_body2.markdown("###### 서비스 민원") 

    # -----------------------------------------------------------------------  
    t1_body3.markdown("###### 서비스2 민원") 

    # -----------------------------------------------------------------------  
    t1_body4.markdown("###### 기타 민원") 