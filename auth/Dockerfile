FROM madhurachanna/ticketing-common:0.08 as common-builder

FROM python:3.8.2
WORKDIR /app
RUN pip install pipenv
COPY ./Pipfile* ./
RUN pipenv install --ignore-pipfile --deploy
COPY ./ ./
COPY --from=common-builder /app/src /app/common/

EXPOSE 5000

CMD pipenv run gunicorn -b :5000 run:app
