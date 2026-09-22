
import streamlit as st
import pandas as pd
st.set_page_config(
    page_title="Smart AI lab - Intro to ML",
    layout="wide"
)
st.sidebar.title("Smart AI Lab")

st.sidebar.write(
    "Explore the basics of Machine Learning and see "
    "how Streamlit can be used to build interactive ML applications."
)

page=st.sidebar.radio(
    "Choose a tipic",
    [
        "Start Here",
        "AI and Machine Learning",
        "How Machines Learn",
        "Types of Machine Learning",
        "Choose the Right Approach",
        "ML in Different Industries",
        "ML Project Lifecycle",
        "Final Chalenge"
    ]
)
if page=="Start Here":
    st.title("Smart AI Lab")
    st.write("""Welcome to the first sessino of our Machine learning journey.
    Imagine that you have joined the analytics team  of a bank.
    The business team dows not start by telling you which
    Machine Learning algorithm to use.
    They start with a business problem.
    """)
    st.divider()
    st.subheader("The bank has three questions")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("### Prediction")
        st.write("""
        Can we precict whether a customer is likely
        to default on a loan?
        """)
    
    with col2:
        st.markdown("### Discovery")
        st.write("""
        Can we discover different types of customers 
        from the data?
        """)
    with col3:
        st.markdown("### Decisions")
        st.write("""
        Can a machine learn which actions is better
        beased on feedback?
        """)
    st.divider()
    st.write("""
    These three questions are all related to Machine Learning,
    but they represent different learning problems.
    
    During this session we will understand the difference
    between them and also see how Streamlit can help use
    turn our ideas into interactive applications.
    """)
    st. info(
        "The goal of this session is understanding, not model building."
    )
elif page=="AI and Machine Learning":
    st.title("Artificial Intelligence and Machine Learning")

    st.write("""
    Before learning Machiine Learning, we need to understand  
    where it fits into the larger field of Artificial Intelligence.
    """)

    st.subheader("Artificial Intelligence")
    st.write("""
    Artificial Intelligence is the boarder field of creating
    computer systems that can perform tasks that normally
    require human intelligence.
    These taskscan include learning, reasoning, perception,
    language understanding, planning and decision-making.
    """)
    st.subheader("Machine Learning")
    st.write("""
    Machine Learning is a subset of Artificial Intelligence.
    Instead of explicitly programming every rule, we provide
    data to a Machine Learning system and allow it to learn 
    patterns from that data. 
    Those learned patterns can then be used to make preedictions,
    identify patterns or suport decisions.
    """)
    st.subheader("Deep Learning")
    st.write("""
    Deep Learning is a subset of Macchine Learning based on 
    multi-layer neural networks.
    It is a particularly useful when working with complex data
    such as images, speech, videa and large amounts of text.
    """)

    st.divider()
    st.markdown("""
    **Artificial Intelligence** - A broad field concerned with intelligent behaviour.
    **Machine Learning** - A family of Machine Learning methods based on
    multi-layered neural networks.
    """)
    st.divider()
    st.subheader("Smart banking")

    st.write("""
    Consider a banking application.
    AI could refer to the overall intelligent system.
    Machine Learning could be used for:
    - prdeicting loan default
    - detecting unusual transaction
    - forecasting demand
    - understanding customer behaviour

    Deep Learning could be useful for:
    - analysing documents
    - speech recognition
    - understanding text
    - image-based document processing
    """)
    
elif page == "How Machines Learn":
    st.title("What Dows It mean for a Machine to Leran?")
    st.write("""
    In traditional programming, we normally provide rules and
    data to produce an output.
    """)

    st.subheader("Traditional programming")

    st.markdown("""
    **Rules + Data = Output**
    """)

    st.write("""
    Example: A programmer may explicity write rules such as:
    If transaction amount is greater than a partiular value
    and the transaction happens in a unusual location,
    flag the transaction.
    This workd well when the rules are known and can be 
    clearly written.
    """)

    st.divider()

    st.subheader("Machine Learning")

    st.markdown("""*Data + Expected outcomes -> Learning Process -> Model*""")

    st.write("""
    In Machine Learning, instead of manually writing every rule, we provide examples to a learning system.
    The system tries to identify patterns in those examples.The result is a model that can be used on new data.
    """)
    st.divider()
    st.subheader("Smart Banking")
    st.write("""
    Suppose a bank has historical customer iinformation.
    For each customer we may have:
    - income
    - age
    - credit history
    - loan amount
    -repayment behaviour
    If we also know whether those customers eventually
    defaulted, we can use those historical examples to 
    learn a relationship between the customer information
    and the outcome.
    """)

    st.write("""
    The important idea is:
    **The model learns from examples rather than being given every rule explicitly.**
    """)