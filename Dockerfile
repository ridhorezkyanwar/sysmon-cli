# 1. Gunakan base image Python resmi yang ringan
FROM python:3.11-slim

# 2. Tentukan direktori kerja di dalam kontainer
WORKDIR /app

# 3. Salin file dependensi dan install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Salin seluruh kode proyek ke dalam kontainer
COPY . .

# 5. Perintah utama untuk menjalankan aplikasi
ENTRYPOINT ["python", "-m", "sysmon_cli"]