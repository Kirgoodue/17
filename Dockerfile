FROM python:3.9-slim
WORKDIR /app
COPY app.py .
COPY wait-for-it.sh .
RUN pip install psycopg2-binary
RUN chmod +x wait-for-it.sh
CMD [ "./wait-for-it.sh", "postgres_db:5432", "--", "python", "app.py" ]