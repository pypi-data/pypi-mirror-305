import os.path

from jl95terceira.pytools.envlib import vars,var

JDK_HOMES:vars.Var[dict[str,str]] \
                 = var(name       ='jdk.homes', 
                       description='a map (dict) of Java homes by version (as a string)',
                       default    =dict())
MAVEN_HOME       = var(name       ='maven.home', 
                       description='the home of Apache Maven')
MAVEN            = var(name       ='maven', 
                       description='the path / alias to Apache Maven executable',
                       default    = os.path.join(MAVEN_HOME.get(), 'bin', 'mvn.exe') if MAVEN_HOME.check() else 'mvn')
ANT_HOME         = var(name       ='ant.home', 
                       description='the home of Apache Ant')
ANT              = var(name       ='ant', 
                       description='the path / alias to Apache Ant executable',
                       default    = os.path.join(ANT_HOME.get(), 'bin', 'mvn.exe') if ANT_HOME.check() else 'ant')
