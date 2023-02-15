indata = '''
< dependencies >
< dependency >
< groupId > org.springframework.boot < / groupId >
< artifactId > spring - boot - starter - data - jpa < / artifactId >
< / dependency >
< dependency >
< groupId > org.springframework.boot < / groupId >
< artifactId > spring - boot - starter - validation < / artifactId >
< / dependency >
< dependency >
< groupId > org.springframework.boot < / groupId >
< artifactId > spring - boot - starter - web < / artifactId >
< / dependency >
< dependency >
< groupId > org.jacoco < / groupId >
< artifactId > jacoco - maven - plugin < / artifactId >
< version >${jacoco - maven - plugin.version} < / version >
< / dependency >
< dependency >
< groupId > com.h2database < / groupId >
< artifactId > h2 < / artifactId >
< scope > runtime < / scope >
< / dependency >
< !--JACKSON -->
< dependency >
< groupId > com.fasterxml.jackson.core < / groupId >
< artifactId > jackson - databind < / artifactId >
< / dependency >
< dependency >
< groupId > com.fasterxml.jackson.dataformat < / groupId >
< artifactId > jackson - dataformat - yaml < / artifactId >
< / dependency >
< !--Logging -->
< dependency >
< groupId > org.springframework.boot < / groupId >
< artifactId > spring - boot - starter < / artifactId >
< exclusions >
< exclusion >
< groupId > org.springframework.boot < / groupId >
< artifactId > spring - boot - starter - logging < / artifactId >
< / exclusion >
< / exclusions >
< / dependency >
< dependency >
< groupId > org.springframework.boot < / groupId >
< artifactId > spring - boot - starter - log4j2 < / artifactId >
< / dependency >

< dependency >
< groupId > org.springframework.boot < / groupId >
< artifactId > spring - boot - starter - test < / artifactId >
< scope > test < / scope >
< / dependency >
< dependency >
< groupId > junit < / groupId >
< artifactId > junit < / artifactId >
< scope > test < / scope >
< / dependency >
< dependency >
< groupId > org.junit.vintage < / groupId >
< artifactId > junit - vintage - engine < / artifactId >
< scope > test < / scope >
< / dependency >
< / dependencies >
'''

for line in indata:
    # out = readlines(line)
    print(line)
