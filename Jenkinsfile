        node{
		
	deleteDir()
        
	stage "Checkout"
        
            	scm()
		
        stage "Build"
		
		build()
		
	stage "Sonar Analysis"
		
		sonar()
		
	stage "ZIP artifacts"

		zip()
		
	stage "Artifactory Upload"
		
		artup()
		
	stage "Download from Artifactory"
		
		artdown()
 
  		}


		def scm(){
		checkout([$class: 'GitSCM', branches: [[name: '*/master']],
        	userRemoteConfigs: [[url: 'https://github.com/vamsimakkena1/cicd1.git']]])
		}

		def build(){
	
		def mavenhome = tool 'maven';

		sh "${mavenhome}/bin/mvn clean package"
		}

		def sonar(){
			
		def scannerHome = tool 'sonar';
		
    		withSonarQubeEnv('localsonar') { 
			
      		sh "${scannerHome}/bin/sonar-scanner -Dproject.settings=/var/vamsi/sonar-scanner.properties "
			
    		}
			
		}

		def zip(){
	
		sh "zip -r dateutils.${BUILD_NUMBER}.zip target"
	
		}

		def artup(){
			
		def uploadSpec =
			
		'''{ 
             	"files": [ 
                 		{ 
                     			"pattern": "dateutils.${BUILD_NUMBER}.zip", 
                     			"target": "my-maven-local" 
                 		} 
            		 ] 
         	}''' 
			
		def server = Artifactory.server "localartifactory"
		
		def buildInfo = server.upload spec: uploadSpec
		
		server.publishBuildInfo buildInfo
			
		}

		def artdown(){
	
		def downloadSpec = 
             
		'''{ 
             	"files": [ 
                 		{ 
                     			"pattern": "my-maven-local/dateutils.${BUILD_NUMBER}.zip", 
                     			"target": "dateutils.zip"
                 		} 
            		 ] 
        	}''' 
 		
		def server = Artifactory.server "localartifactory"
 
     		def buildInfo1 = server.download spec: downloadSpec
		
		server.publishBuildInfo buildInfo1
 
  		}
