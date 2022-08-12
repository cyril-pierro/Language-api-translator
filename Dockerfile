FROM python:3.9-slim-buster
RUN mkdir /model
WORKDIR /app
COPY . /app/
ENV MODEL_PATH=/model/model.pt
RUN pip install poetry
RUN poetry install 
RUN echo "Training model....."
RUN echo "import torch" >> script.py
RUN echo "from happytransformer import HappyTextToText, TTSettings" >> script.py
RUN echo "model = HappyTextToText('T5', 't5-base')" >> script.py
RUN echo "torch.save(model, '/model/model.pt')" >> script.py
RUN python script.py

EXPOSE 8000
ENTRYPOINT [ "uvicorn","main:app --reload"]

