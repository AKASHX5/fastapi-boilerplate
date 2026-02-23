FROM python:3.12
ARG INSTALL_DEV=false
WORKDIR /src

# Set dynamic environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

RUN if [ "$INSTALL_DEV" = "true" ] ; then pip install pytest debugpy ; fi

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]