import pickle
import streamlit as st

# Membaca Model
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

# Menambahkan Gambar atau Logo
st.image("gambar_diabetes.jpg", use_column_width=True)

# Judul dan Deskripsi
st.title('Aplikasi Prediksi Diabetes')
st.write("""
Aplikasi ini menggunakan algoritma **Support Vector Machine (SVM)** untuk memprediksi apakah seseorang terkena diabetes berdasarkan beberapa parameter kesehatan.
Silakan masukkan nilai-nilai di bawah ini dan klik **Test Prediksi Diabetes** untuk melihat hasilnya.
""")

# Membagi menjadi 2 kolom
col1, col2 = st.columns(2)

with col1:
    Pregnancies = st.number_input(
        'Input Nilai Pregnancies', min_value=0, max_value=20, value=0)
with col2:
    Glucose = st.number_input('Input Nilai Glucose',
                              min_value=0, max_value=200, value=0)
with col1:
    BloodPressure = st.number_input(
        'Input Nilai Blood Pressure', min_value=0, max_value=150, value=0)
with col2:
    SkinThickness = st.number_input(
        'Input Nilai Skin Thickness', min_value=0, max_value=100, value=0)
with col1:
    Insulin = st.number_input('Input Nilai Insulin',
                              min_value=0, max_value=900, value=0)
with col2:
    BMI = st.number_input('Input Nilai BMI', min_value=0.0,
                          max_value=70.0, value=0.0)
with col1:
    DiabetesPedigreeFunction = st.number_input(
        'Input Nilai Diabetes Pedigree Function', min_value=0.0, max_value=3.0, value=0.0)
with col2:
    Age = st.number_input('Input Nilai Age', min_value=0,
                          max_value=120, value=0)

# Membuat button untuk prediksi di bawah input Age
if st.button('Test Prediksi Diabetes'):
    with st.spinner('Sedang memproses...'):
        # Konversi input ke float
        input_data = [
            float(Pregnancies), float(Glucose), float(BloodPressure),
            float(SkinThickness), float(Insulin), float(BMI),
            float(DiabetesPedigreeFunction), float(Age)
        ]

        # Prediksi
        diab_prediction = diabetes_model.predict([input_data])

        # Menampilkan hasil prediksi
        if diab_prediction[0] == 1:
            st.error('Pasien Terkena Diabetes')
        else:
            st.success('Pasien Tidak Terkena Diabetes')

# Menambahkan informasi tambahan di sidebar (opsional)
st.sidebar.write("""
### Tentang Aplikasi
Aplikasi ini dibuat menggunakan:
- **Python**
- **Streamlit**
- **Scikit-learn** (SVM)
""")

# Menambahkan footer
st.markdown("---")
st.write("© 2025 Aplikasi Prediksi Diabetes. Dibuat dengan ❤️ oleh PeterFranklin.")
