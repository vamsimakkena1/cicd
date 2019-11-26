        node{
        
	stage "Checkout"
        
            checkout([$class: 'GitSCM', branches: [[name: '*/master']],
            userRemoteConfigs: [[url: 'https://github.com/vamsimakkena1/cicd1.git']]])
            
        stage "Build"

             sh "/usr/local/apache-maven-3.2.2/bin/mvn clean install"
         
         }
        
    