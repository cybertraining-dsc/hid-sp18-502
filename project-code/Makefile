SWAGGERCODEGEN=java -jar swagger-codegen-cli-2.3.1.jar
YAMLFILE=azure.yaml
DESTDIR=server/azure/flaskConnexion
CREATED=server

all: service start 
	@echo "DONE"

docker-all: docker-build docker-start 
	@echo "DONE"

docker-build:
	@echo "building the image from docker file..."
	docker build --no-cache -t cloudmesh/azure .
	@echo "image DONE"

docker-pull:
	@echo "pulling the image from dockerhub..."
	docker pull cloudmesh/azure
	@echo "image DONE"

docker-start:
	@echo "starting the service in container..."
	docker run -p 8080:8080 cloudmesh/azure


docker-stop:
	@echo "stoping the service..."
	docker stop $$(docker ps -alq)
	@echo "service stopped"

docker-remove:
	@echo "removing the image..."
	docker rmi -f cloudmesh/azure
	@echo "image removed"

docker-clean: docker-stop docker-remove
	@echo "DONE"

dest:
	mkdir -p $(DESTDIR)
	 
service: dest
	@echo "creating the service..."
	wget http://central.maven.org/maven2/io/swagger/swagger-codegen-cli/2.3.1/swagger-codegen-cli-2.3.1.jar
	$(SWAGGERCODEGEN) generate \
	-i $(YAMLFILE) \
	-l python-flask \
	-o $(DESTDIR) 
	-D supportPython3=true
	
	rm *.jar
	pip install --upgrade pip
	pip install azure
	
	cp -r *.py $(DESTDIR)/swagger_server/models
	cp default_controller.py $(DESTDIR)/swagger_server/controllers

	cd $(DESTDIR) && pip install -r requirements.txt && \
	python setup.py install 
	
	

start:  
	@echo "starting the service..."
	cd $(DESTDIR) && python -m swagger_server

test:
	curl http://localhost:8080/cloudmesh/azure/resourcegroup/create/sample

            
stop:
	@echo "stopping the service"
	ps -ef | grep swagger_server | grep -v "grep" | awk '{print $$2}' | xargs kill -9
	@echo "service stopped"

clean:
	@echo "removing service files created"
	rm -rf $(CREATED)
