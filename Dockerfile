FROM python:3.9

WORKDIR /app
ENV FLASK_APP app
ENV FLASK_ENV production

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 8050

# CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=8050"]
CMD [ "python3", "app.py"]