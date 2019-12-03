        node{
        
	stage "Checkout"
        
            checkout([$class: 'GitSCM', branches: [[name: '*/master']],
            userRemoteConfigs: [[url: 'https://github.com/vamsimakkena1/cicd1.git']]])
            
        stage "Build"

             sh "/usr/bin/apache-maven-3.6.3/bin/mvn clean install"
         
         }
        
    
