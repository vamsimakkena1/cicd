        node("Slave"){
            
		
	deleteDir()
        
	stage("Checkout"){
        
            	scm()
	}
		
    stage("Build"){
		
		build()
    }	
	//stage("Sonar Analysis"){
		
	//	sonar()
	//}
	//stage('Publish test results') {
	    
      //junit '**/test-results/test/*.xml'
      
    //} 
	//stage "ZIP artifacts"

	//	zip()
		
	//stage("Artifactory Upload"){
		
	//	artup()
		//buildNumber: '${BUILD_NUMBER}'
	//}
	
	//stage("Download from Artifactory"){
		
	//	artdown()
		//buildNumber: '${BUILD_NUMBER}'
	//}
    //stage("Upload to s3"){
        
       // withAWS(credentials: 'laaws', region: 'us-east-1') {
            
            //s3Upload(bucket:"lavamsi", workingDir:'.', includePathPattern:'*');
            
        //}
    //}
  	}


		def scm(){
		    
		checkout([$class: 'GitSCM', branches: [[name: '*/master']],
        	userRemoteConfigs: [[url: 'https://github.com/vamsimakkena1/cicd1.git']]])
		}

		def build(){
	
		def mavenhome = tool 'm2_3.6.3';
        
		sh "${mavenhome}/bin/mvn clean package -DskipTests=true"

		}
		def sonar(){
			
		def scannerHome = tool 'sonar';
		
    		withSonarQubeEnv('localsonar') { 
			
      		sh "${scannerHome}/bin/sonar-scanner -Dsonar.projectKey=test -Dsonar.sources=src/ -Dsonar.java.binaries=target/"
      		//-Dproject.settings=/var/vamsi/sonar-scanner.properties "
			
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
                     			"pattern": "target/dateutils-bundle.tar", 
                     			"target": "my-maven-local"
                 		} 
            		 ] 
         	}''' 
		buildNumber: '${BUILD_NUMBER}'
		
		def server = Artifactory.server "localartifactory"
		
		def buildInfo = server.upload spec: uploadSpec
		
		server.publishBuildInfo buildInfo
			
		}

		def artdown(){
		def downloadSpec = 
             
		'''{ 
             	"files": [ 
                 		{ 
                     			"pattern": "my-maven-local/dateutils-bundle.tar", 
                     			"target": "dateutils.tar"
                     			
                 		} 
            		 ] 
        	}''' 
 		
 		buildNumber: '${BUILD_NUMBER}'
 		
		def server = Artifactory.server "localartifactory"
 
     		def buildInfo1 = server.download spec: downloadSpec
		
	    server.publishBuildInfo buildInfo1
 
  		
		}
		
		//https://www.guru99.com/maven-jenkins-with-selenium-complete-tutorial.html
