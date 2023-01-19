lorem = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut aliquet odio lacus, eu aliquam enim congue ut. Integer viverra sit amet eros sit amet auctor. Etiam tincidunt dui eget aliquet scelerisque. Duis leo nulla, tempor vitae leo at, dictum tempus lorem. Quisque iaculis bibendum libero, eget faucibus tortor mollis vitae. Fusce vel leo nec nibh dictum facilisis vitae nec est. Quisque varius sodales commodo. Vestibulum tristique, mauris ac maximus dapibus, mauris ex efficitur lorem, efficitur vulputate mi quam ut diam. Maecenas id pellentesque ex, a suscipit ipsum. Aliquam condimentum venenatis ligula, id euismod est. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Donec mattis nisi sed lacus tempus imperdiet. Donec tempus lorem vel nisi vestibulum lacinia. Aenean ultricies laoreet justo eu ornare. Sed lorem erat, maximus ut commodo sit amet, sodales sit amet risus.

Vestibulum sed iaculis justo. Aenean gravida lobortis enim at pretium. Suspendisse auctor est at dolor malesuada, in cursus quam scelerisque. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Nulla pharetra facilisis est, faucibus lacinia arcu condimentum et. Etiam at dapibus lorem. Mauris mauris nunc, fermentum et mauris eu, laoreet posuere erat. Vestibulum porttitor eget augue quis condimentum.

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec auctor molestie ipsum at vehicula. In id sem et velit cursus consequat. Curabitur eleifend ipsum nibh, id imperdiet arcu pulvinar tempus. Integer in rhoncus ipsum, vel egestas felis. Integer lobortis, ante ac volutpat porta, ante ipsum commodo arcu, ut fringilla nulla nisi in eros. Proin rutrum nibh est. Nullam ex urna, aliquet at enim sed, feugiat tincidunt nisl. Nullam ut diam magna. Nam placerat, felis eget rutrum porttitor, est libero vulputate diam, sit amet scelerisque tortor odio a nunc. Maecenas hendrerit sodales nisl. Nullam quis molestie tortor, eu tincidunt ligula. Quisque at tellus sed tellus laoreet mollis eget non purus. Integer scelerisque finibus odio ac scelerisque. Vivamus fermentum sapien sed enim placerat, sit amet elementum ipsum scelerisque.

Donec congue dictum nibh, non aliquet magna fermentum ac. Fusce eu eleifend arcu, eget fermentum dui. Duis at aliquet enim. Praesent maximus nunc urna, sit amet dictum sapien ultricies in. Donec ultrices ut purus eu varius. Etiam et arcu nec orci suscipit consequat sit amet ut nulla. Aliquam varius metus nisl, nec vehicula nisi sollicitudin ut. In ut luctus nibh. Quisque sed venenatis enim, molestie sollicitudin nibh. Maecenas in arcu interdum, iaculis lectus in, tempor tortor. Sed ante nisi, maximus id molestie a, sagittis faucibus turpis. Duis nisl leo, lobortis eget gravida eget, posuere id nibh. Fusce iaculis risus est, non elementum ex lacinia eu. Curabitur ligula dolor, ullamcorper quis ante eu, gravida porta mi. Donec at aliquet velit.

Curabitur dapibus congue lorem, vitae interdum massa viverra eget. Suspendisse tincidunt vitae purus non efficitur. Maecenas sed rhoncus lorem. Fusce leo orci, mollis quis risus quis, faucibus facilisis urna. Cras et mauris imperdiet dui venenatis feugiat. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam interdum aliquam ante pellentesque ullamcorper. Pellentesque eget nisi suscipit, gravida massa varius, cursus libero. Phasellus sit amet venenatis tortor. Morbi scelerisque lacus in ante pretium, id venenatis mauris vehicula. Nullam vehicula turpis ac arcu commodo, eget sagittis nisl tincidunt. Pellentesque vel cursus nibh. Pellentesque porttitor ligula ex, in dapibus metus scelerisque ut. Maecenas a maximus sapien, non mattis lorem. Sed hendrerit tellus sit amet efficitur commodo.'''

table = {}

for char in lorem:
    if char in table:
        table[char] += 1
    
    else:
        table[char] = 1

print(table)
