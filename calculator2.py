import streamlit as st

st.set_page_config(layout="wide")

def main():
    st.title("- Einfacher Rechner mit Streamlit -")

    # Initialisierung von session_state für Zahl1 und das Log
    if "zahl1" not in st.session_state:
        st.session_state.zahl1 = 0.0
    if "history" not in st.session_state:
        st.session_state.history = []  # Liste für die Historie

    col1, col2, col3 = st.columns([4, 1, 4])

    with col1:
        zahl1 = st.number_input("Zahl1", value=st.session_state.zahl1, format="%.2f", key="zahl1_input")

    with col2:
        operation = st.selectbox("Operator", ["+", "-", "*", "/", "Exp", "√"], index=0)

    with col3:
        zahl2 = st.number_input("Zahl2", value=0.0, format="%.2f")

    # Spalten für Buttons
    col1, col2 = st.columns(2)

    with col1:
        if st.button("Berechnen"):
            ergebnis = None

            # Berechnung
            if operation == "+":
                ergebnis = zahl1 + zahl2
            elif operation == "-":
                ergebnis = zahl1 - zahl2
            elif operation == "*":
                ergebnis = zahl1 * zahl2
            elif operation == "Exp":
                ergebnis = zahl1 ** zahl2
            elif operation == "√":
                ergebnis = pow(zahl1, 1 / zahl2) if zahl2 != 0 else None
            elif operation == "/":
                ergebnis = zahl1 / zahl2 if zahl2 != 0 else None

            # Ergebnis anzeigen und speichern
            if ergebnis is not None:
                st.session_state.zahl1 = ergebnis  # Speichern für die nächste Rechnung

                # Speichern in der History
                log_entry = f"{zahl1} {operation} {zahl2} = {ergebnis}"
                st.session_state.history.append(log_entry)

                # Aktuelle Berechnung anzeigen
                st.markdown(f"### **{log_entry}**")
            else:
                st.error("Fehler: Ungültige Berechnung!")

    with col2:
        if st.button("Alles löschen"):
            st.session_state.zahl1 = 0.0  # Zurücksetzen von Zahl1
            st.session_state.history = []  # Verlauf leeren
            st.rerun()  # Seite neu laden, um die Änderungen anzuzeigen

    # Berechnungsverlauf anzeigen
    if st.session_state.history:
        st.subheader("Berechnungsverlauf:")
        for entry in reversed(st.session_state.history):  # Neueste zuerst
            st.write(entry)

if __name__ == "__main__":
    main()
