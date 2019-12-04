        node{
        
	stage "Checkout"
        
        	checkout([$class: 'GitSCM', branches: [[name: '*/master']],
        	userRemoteConfigs: [[url: 'https://github.com/vamsimakkena1/cicd1.git']]])
            
        stage "Build"

        	sh "/usr/apache-maven-3.6.3/bin/mvn clean install"
		
	stage "Sonar Analysis"
		
		def scannerHome = tool 'sonar';
		
    		withSonarQubeEnv('localsonar') { 
			
      		sh "${scannerHome}/bin/sonar-scanner"
			
    			}
  		}

		
          }
        
    
