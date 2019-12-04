        node{
        
	stage "Checkout"
        
            checkout([$class: 'GitSCM', branches: [[name: '*/master']],
            userRemoteConfigs: [[url: 'https://github.com/vamsimakkena1/cicd1.git']]])
            
        stage "Build"

             sh "mvn clean install"
         
         }
        
    
