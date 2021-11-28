FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Install Tkinter
RUN apt-get install tk -y

COPY . .

CMD [ "python", "./main.py" ]