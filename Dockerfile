FROM python:3.7-slim

WORKDIR /app

COPY requirements-d.txt ./requirements.txt

RUN pip install -r requirements.txt

EXPOSE 8501

COPY . .

ENTRYPOINT ["streamlit", "run"]

CMD ["./streamlitui/app.py"]
# CMD streamlit run ./streamlitui/app.py