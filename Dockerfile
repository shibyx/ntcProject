FROM python
WORKDIR /app
COPY . .

RUN pip install Flask
RUN pip install pytz

EXPOSE 5000

CMD [ "python", "main.py" ]
