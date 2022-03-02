FROM python
WORKDIR /app
COPY . .

RUN pip install Flask

EXPOSE 5000

CMD [ "python", "main.py" ]

