# Much like inheriting from a parent class, we can inherit all the components (e.g. utility software) of a parent environment, and its parent (in this case a base OS image).
 # In this case, we inherit a self-contained Linux environment with Python 3 installed.
FROM python:3

# Create and move to a working directory within the image (good practice; this is a standard path).
WORKDIR /usr/src/app

# Copy everything from the current local directory (where the Dockerfile exists) to the container (within the working directory).
# Really we should be more selective here (e.g. have some files ignored via a .dockerignore file).
COPY . .

# Document that containers created from this image should open port 8888 (this port can also be actually published, by adding a flag when running the container).
EXPOSE 8888

# Ensure that output from the program is not buffered, so we can see the output.
ENV PYTHONUNBUFFERED=1

# Run the program itself within the container, as we would on the command line.
CMD ["python", "main.py"]
