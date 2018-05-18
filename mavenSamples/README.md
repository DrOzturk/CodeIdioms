
```bash
cd result
mvn archetype:generate
```
select default app type, currently it is
```bash
11: org.apache.maven.archetypes:maven-archetype-quickstart (An archetype which contains a sample Maven project.)
```
give package names etc.
ex:
   app name: HelloMvnApp
   version: 1.0-SNAPSHOT
   package name: com.drozturk.hellomvn

creates HelloMvnApp folder, with pom.xml in it.

```bash
cd HelloMvnApp
mvn compile
mvn package # also runs tests
java -cp target/HelloMvnApp-1.0-SNAPSHOT.jar com.drozturk.hellomvn.App
```
Prints 
Hello World! 