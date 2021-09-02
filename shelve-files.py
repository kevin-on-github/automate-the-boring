import shelve


f = shelve.open('myshelvefile')
# f['LinuxOS'] = ['AlmaLinux', 'CentOS Stream', 'Debian', 'Ubuntu'] # Write data to shelve file.
print(f['LinuxOS'])
print(list(f.keys()))
print(list(f.values()))
f.close()

