FROM python:3.9-slim-buster
RUN mkdir /model
WORKDIR /app
COPY . /app/
COPY pyproject.toml  /app/
ENV MODEL_PATH=/model/model.pt
ENV PYTHONPATH=${PYTHONPATH}:${PWD}
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install 
RUN echo "Download model....."
RUN echo "from happytransformer import HappyTextToText, TTSettings" >> script.py
RUN echo "model = HappyTextToText('T5', 't5-base')" >> script.py
RUN echo "model.save('/model/model.pt')" >> script.py
RUN poetry run python3 script.py
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8080"]

