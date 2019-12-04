        node{
		
	deleteDir()
		
	def server = Artifactory.server "localartifactory"
        
	stage "Checkout"
        
        	checkout([$class: 'GitSCM', branches: [[name: '*/master']],
        	userRemoteConfigs: [[url: 'https://github.com/vamsimakkena1/cicd1.git']]])
            
        stage "Build"
		
		def mavenhome = tool 'maven';

		sh "${mavenhome}/bin/mvn clean install"
		
	stage "Sonar Analysis"
		
		def scannerHome = tool 'sonar';
		
    		withSonarQubeEnv('localsonar') { 
		
			
      		sh "${scannerHome}/bin/sonar-scanner -Dproject.settings=/var/vamsi/sonar-scanner.properties "
			
    			}
	stage "ZIP artifacts"
		
		sh "zip -r dateutils.${BUILD_NUMBER}.zip target"
		
	stage "Artifactory Upload"
		
		def uploadSpec =
			
		'''{ 
             	"files": [ 
                 		{ 
                     			"pattern": "dateutils.${BUILD_NUMBER}.zip", 
                     			"target": "my-maven-local" 
                 		} 
            		 ] 
         	}''' 
		
		def buildInfo = server.upload spec: uploadSpec
		
		server.publishBuildInfo buildInfo
		
	stage "Download from Artifactory"
		def downloadSpec = 
             
		'''{ 
             	"files": [ 
                 		{ 
                     			"pattern": "my-maven-local/dateutils.${BUILD_NUMBER}.zip", 
                     			"target": "dateutils.zip"
                 		} 
            		 ] 
        	}''' 
 
 
     		//def buildInfo1 = server.download spec: downloadSpec 

 
  		}
