FROM python:3.7
EXPOSE 8501
WORKDIR /app
COPY requirements.txt ./requirements.txt

RUN apt update && apt install -y sudo
RUN pip3 install -r requirements.txt

COPY . .

CMD streamlit run pass_gen.py
