FROM python:3.8
EXPOSE 7860
WORKDIR /tonality_prediction
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
