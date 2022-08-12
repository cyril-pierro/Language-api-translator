FROM python:3.9-slim-buster
RUN mkdir /model
WORKDIR /app
COPY . /app/
RUN pip install uvicorn
RUN export MODEL_PATH=/model/model.pt
RUN pip install poetry
RUN  poetry env use python3
RUN poetry install 
RUN echo "Download model....."
RUN echo "from happytransformer import HappyTextToText, TTSettings" >> script.py
RUN echo "model = HappyTextToText('T5', 't5-base')" >> script.py
RUN echo "model.save('/model/model.pt')" >> script.py
RUN poetry run python3 script.py
EXPOSE 8000
CMD ["uvicorn", "main:app --reload"]

