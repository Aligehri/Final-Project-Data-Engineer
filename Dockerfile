FROM python:3.12.5

RUN mkdir Proyecto_Final
RUN cd Proyecto_Final

WORKDIR /Proyecto_Final

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["/bin/bash"]
