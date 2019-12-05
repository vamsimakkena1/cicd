        node{
		
	deleteDir()
		
	def server = Artifactory.server "localartifactory"
        
	stage "Checkout"
        
        	//checkout([$class: 'GitSCM', branches: [[name: '*/master']],
        	//userRemoteConfigs: [[url: 'https://github.com/vamsimakkena1/cicd1.git']]])
            	scm()
        stage "Build"
		
		//def mavenhome = tool 'maven';

		//sh "${mavenhome}/bin/mvn clean install"
		build()
	stage "Sonar Analysis"
		
		//def scannerHome = tool 'sonar';
		
    		//withSonarQubeEnv('localsonar') { 
		
			
      		//sh "${scannerHome}/bin/sonar-scanner -Dproject.settings=/var/vamsi/sonar-scanner.properties "
			
    		//	}
		
		sonar()
	stage "ZIP artifacts"
		
		//sh "zip -r dateutils.${BUILD_NUMBER}.zip target"
		zip()
		
	stage "Artifactory Upload"
		
		//def uploadSpec =
			
		//'''{ 
             	//"files": [ 
                 //		{ 
                  //   			"pattern": "dateutils.${BUILD_NUMBER}.zip", 
                   // 			"target": "my-maven-local" 
                 //		} 
            	//	 ] 
         	//}''' 
		
		//def buildInfo = server.upload spec: uploadSpec
		
		//server.publishBuildInfo buildInfo
		
		artup()
		
	stage "Download from Artifactory"
		
	//	def downloadSpec = 
             
	//	'''{ 
        //     	"files": [ 
        //         		{ 
        //             			"pattern": "my-maven-local/dateutils.${BUILD_NUMBER}.zip", 
        //             			"target": "dateutils.zip"
        //         		} 
        //    		 ] 
        //	}''' 
 
 
     	//	def buildInfo1 = server.download spec: downloadSpec
		
	//	server.publishBuildInfo buildInfo1
		
		artdown()
 
  		}

		def scm(){
		checkout([$class: 'GitSCM', branches: [[name: '*/master']],
        	userRemoteConfigs: [[url: 'https://github.com/vamsimakkena1/cicd1.git']]])
		}

		def build(){
	
		def mavenhome = tool 'maven';

		sh "${mavenhome}/bin/mvn clean install"
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
 
 
     		def buildInfo1 = server.download spec: downloadSpec
		
		server.publishBuildInfo buildInfo1
 
  		}
