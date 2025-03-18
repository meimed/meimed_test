import streamlit as st
st.set_page_config(layout="wide")

def main():
    st.title("Einfacher Rechner mit Streamlit")
    
    col1, col2, col3 =st.columns([4, 1, 4])
    with col1:
        zahl1 = st.number_input("Zahl1",value=0.0, format="%.2f")
    with col2:
        operation = st.selectbox("Operator", ["+", "-", "*", "/","Exp","√"], index=0)
    with col3:
        zahl2 = st.number_input("Zahl2",value=0.0, format="%.2f")

    # Automatische Berechnung
    ergebnis = None
    if operation == "+":
        ergebnis = zahl1 + zahl2
    elif operation == "-":
        ergebnis = zahl1 - zahl2
    elif operation == "*":
        ergebnis = zahl1 * zahl2
    elif operation == "Exp":
        ergebnis = zahl1 ** zahl2
    elif operation == "√":
        if zahl2 !=0:
            ergebnis = pow(zahl1,1/zahl2)
        else:
            st.error("Wurzel aus 0 nicht erlaubt")
    elif operation == "/":
        if zahl2 != 0:
            ergebnis = zahl1 / zahl2
        else:
            st.error("Fehler: Division durch Null ist nicht erlaubt!")

    # Ergebnis anzeigen (nur wenn gültig)
    if ergebnis is not None:
        st.success(f"Das Ergebnis ist: {ergebnis}")
if __name__ == "__main__":
    main()
