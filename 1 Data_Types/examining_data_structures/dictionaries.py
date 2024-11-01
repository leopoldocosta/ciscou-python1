import netmiko 

csr1kv1_connection_info = {
    'ip' : '10.254.0.1',
    'device_type' : 'cisco_ios',
    'username' : 'cisco',
    'password' : 'cisco',
    'port' : 22
}

# net_connect = netmiko.ConnectHandler( 
#     ip=csr1kv1_connection_info['ip'],  
#     device_type=csr1kv1_connection_info['device_type'], 
#     username=csr1kv1_connection_info['username'],  
#     password=csr1kv1_connection_info['password'],  
#     port=csr1kv1_connection_info['port']) 

net_connect = netmiko.ConnectHandler(**csr1kv1_connection_info)

print(net_connect.send_command('show run'))

""" student@student-vm:~/lab_work$ python dictionaries.py 
Building configuration...

Current configuration : 7058 bytes
!
! Last configuration change at 17:55:20 PDT Mon Oct 28 2024
!
version 17.9
service timestamps debug datetime localtime show-timezone
service timestamps log datetime localtime show-timezone
service call-home
platform qfp utilization monitor load 80
platform punt-keepalive disable-kernel-core
platform console virtual
!
hostname csr1kv1
!
boot-start-marker
boot-end-marker
!
!
no logging console
aaa new-model
!
!
aaa authentication login default local
aaa authorization exec default local 
!
!
aaa session-id common
clock timezone PST -8 0
clock summer-time PDT recurring
!
!
!
!
!
!
!
ip domain name cisco.com
!
!
!
login on-success log
!
!
!
!
!
!
!
subscriber templating
! 
! 
! 
! 
!
!
!
multilink bundle-name authenticated
!
!
!
!
!
!
!
!
crypto pki trustpoint TP-self-signed-469090668
 enrollment selfsigned
 subject-name cn=IOS-Self-Signed-Certificate-469090668
 revocation-check none
 rsakeypair TP-self-signed-469090668
!
crypto pki trustpoint SLA-TrustPoint
 enrollment pkcs12
 revocation-check crl
!
!
crypto pki certificate chain TP-self-signed-469090668
 certificate self-signed 01
  3082032E 30820216 A0030201 02020101 300D0609 2A864886 F70D0101 05050030 
  30312E30 2C060355 04031325 494F532D 53656C66 2D536967 6E65642D 43657274 
  69666963 6174652D 34363930 39303636 38301E17 0D323231 31313431 37333430 
  345A170D 33323131 31333137 33343034 5A303031 2E302C06 03550403 1325494F 
  532D5365 6C662D53 69676E65 642D4365 72746966 69636174 652D3436 39303930 
  36363830 82012230 0D06092A 864886F7 0D010101 05000382 010F0030 82010A02 
  82010100 AF1037E6 2E686484 86AF75DA 05C4BE97 9427C1A2 082A8D0E DB987B04 
  D9EA8186 1345A144 7BBB338A BBE3C6DC 15C87690 6B53E84F 0FA58DFA C1A7DC4A 
  AF2E6620 616F2549 D8CDCAFD 5B3357B4 F79EBA94 1E0DD169 386C5AA9 15CE052D 
  EA45D41B 47871299 528585F0 FE353A36 FF3801B2 9D47A982 D68BB104 CE768363 
  E3B20203 580F3831 F9FEDEED EECA5117 14DF4F35 B45B95E5 4A6D57FD C5BBA52F 
  5FE7CAC3 5DE6D767 58FFEBC3 4DA3D55E 5E519E3E 7834DF81 53365A58 7CF7BC76 
  7DB64FE5 E4E2C573 D29F30CC 0AC83BD9 A042E5D8 76AC6731 E8AF13EA EC131D31 
  6FF320DB 5340AF10 9E2610E8 CD80F74A 7A147818 C0F85F2D E89B9FB4 C868C15E 
  DF63805B 02030100 01A35330 51300F06 03551D13 0101FF04 05300301 01FF301F 
  0603551D 23041830 16801496 95C45B64 6BEAC797 CE7CB2B0 65513781 62DCD230 
  1D060355 1D0E0416 04149695 C45B646B EAC797CE 7CB2B065 51378162 DCD2300D 
  06092A86 4886F70D 01010505 00038201 01003F72 1FACDF74 4DF95C7F D8FB2641 
  EBA79B02 487F1660 525ED578 0049626B 715C678A 42037337 EB2692F1 8D0501C9 
  034536BB C0D254AE 862B9EEE 6F54B485 3B877AC2 A93E2FE5 161AD372 3D8E90C6 
  0D7A0084 A6473F6D 5E74A9B8 F06708C4 615B1744 AA03C1A6 9F5780AF B455C1BB 
  E0FA04B8 22D29CA2 D361E903 6F841C1E 865502EB 54330BBF 0AD1A8BA 132325AE 
  BEBB61CA CC047B51 421BA2BF 445C0D6E 66738386 A5174E54 C8AFBEFC 7238DE5B 
  31CF3C48 5BE26CF1 8CF23378 8194483D EDF96C58 EBEDEA0C BCF53297 6DAB7A3D 
  BC4629F5 09EE20BF 93F793E7 D6A7697B 341364EC F7B5EE5F A8AFE360 4B783B54 
  3E9B682D 5FC2C514 C77CE9A6 5C805975 52E5
        quit
crypto pki certificate chain SLA-TrustPoint
 certificate ca 01
  30820321 30820209 A0030201 02020101 300D0609 2A864886 F70D0101 0B050030 
  32310E30 0C060355 040A1305 43697363 6F312030 1E060355 04031317 43697363 
  6F204C69 63656E73 696E6720 526F6F74 20434130 1E170D31 33303533 30313934 
  3834375A 170D3338 30353330 31393438 34375A30 32310E30 0C060355 040A1305 
  43697363 6F312030 1E060355 04031317 43697363 6F204C69 63656E73 696E6720 
  526F6F74 20434130 82012230 0D06092A 864886F7 0D010101 05000382 010F0030 
  82010A02 82010100 A6BCBD96 131E05F7 145EA72C 2CD686E6 17222EA1 F1EFF64D 
  CBB4C798 212AA147 C655D8D7 9471380D 8711441E 1AAF071A 9CAE6388 8A38E520 
  1C394D78 462EF239 C659F715 B98C0A59 5BBB5CBD 0CFEBEA3 700A8BF7 D8F256EE 
  4AA4E80D DB6FD1C9 60B1FD18 FFC69C96 6FA68957 A2617DE7 104FDC5F EA2956AC 
  7390A3EB 2B5436AD C847A2C5 DAB553EB 69A9A535 58E9F3E3 C0BD23CF 58BD7188 
  68E69491 20F320E7 948E71D7 AE3BCC84 F10684C7 4BC8E00F 539BA42B 42C68BB7 
  C7479096 B4CB2D62 EA2F505D C7B062A4 6811D95B E8250FC4 5D5D5FB8 8F27D191 
  C55F0D76 61F9A4CD 3D992327 A8BB03BD 4E6D7069 7CBADF8B DF5F4368 95135E44 
  DFC7C6CF 04DD7FD1 02030100 01A34230 40300E06 03551D0F 0101FF04 04030201 
  06300F06 03551D13 0101FF04 05300301 01FF301D 0603551D 0E041604 1449DC85 
  4B3D31E5 1B3E6A17 606AF333 3D3B4C73 E8300D06 092A8648 86F70D01 010B0500 
  03820101 00507F24 D3932A66 86025D9F E838AE5C 6D4DF6B0 49631C78 240DA905 
  604EDCDE FF4FED2B 77FC460E CD636FDB DD44681E 3A5673AB 9093D3B1 6C9E3D8B 
  D98987BF E40CBD9E 1AECA0C2 2189BB5C 8FA85686 CD98B646 5575B146 8DFC66A8 
  467A3DF4 4D565700 6ADF0F0D CF835015 3C04FF7C 21E878AC 11BA9CD2 55A9232C 
  7CA7B7E6 C1AF74F6 152E99B7 B1FCF9BB E973DE7F 5BDDEB86 C71E3B49 1765308B 
  5FB0DA06 B92AFE7F 494E8A9E 07B85737 F3A58BE1 1A48A229 C37C1E69 39F08678 
  80DDCD16 D6BACECA EEBC7CF9 8428787B 35202CDC 60E4616A B623CDBD 230E3AFB 
  418616A9 4093E049 4D10AB75 27E86F73 932E35B5 8862FDAE 0275156F 719BB2F0 
  D697DF7F 28
        quit
!
!
!
!
!
!
!
!
license udi pid C8000V sn 9URYNQ2VLHN
license boot level network-advantage addon dna-advantage
no diagnostic bootup level
memory free low-watermark processor 63718
!
!
spanning-tree extend system-id
!
enable secret 9 $9$M8M0ivq8lM3puE$mXV/ku3AoYBor3.IKbcvZOpqHFyeyNe2ZlqtCbxgWZg
!
!
username cisco privilege 15 secret 9 $9$JxZVj.IvcNjZa.$lMuMoH5kBBPWV3w9mUv/n9WukVb8l6UefnAAKSxi8uA
!
redundancy
!
!
!
!
!
!
! 
!
!
!
!
!
!
!
!
!
!
!
!
!
! 
! 
!
!
interface GigabitEthernet1
 no ip address
 negotiation auto
 no mop enabled
 no mop sysid
!
interface GigabitEthernet2
 ip address 10.12.0.1 255.255.255.0
 negotiation auto
 no mop enabled
 no mop sysid
!
interface GigabitEthernet3
 ip address 10.13.0.1 255.255.255.0
 negotiation auto
 no mop enabled
 no mop sysid
!
interface GigabitEthernet4
 ip address 10.254.0.1 255.255.255.0
 negotiation auto
 no mop enabled
 no mop sysid
!
ip forward-protocol nd
ip http server
ip http authentication local
ip http secure-server
!
ip route 10.23.0.2 255.255.255.255 10.12.0.2
ip route 10.23.0.3 255.255.255.255 10.13.0.3
ip ssh version 2
ip scp server enable
!
!
logging history size 500
logging history debugging
!
!
!
!
!
!
control-plane
!
!
mgcp behavior rsip-range tgcp-only
mgcp behavior comedia-role none
mgcp behavior comedia-check-media-src disable
mgcp behavior comedia-sdp-force disable
!
mgcp profile default
!
!
!
!
!
!
line con 0
 exec-timeout 120 0
 privilege level 15
 logging synchronous
 stopbits 1
line aux 0
line vty 0 4
 exec-timeout 720 0
 privilege level 15
 transport preferred none
 transport input ssh
line vty 5 15
 exec-timeout 720 0
 privilege level 15
 transport preferred none
 transport input ssh
!
call-home
 ! If contact email address in call-home is configured as sch-smart-licensing@cisco.com
 ! the email address configured in Cisco Smart License Portal will be used as contact email address to send SCH notifications.
 contact-email-addr sch-smart-licensing@cisco.com
 profile "CiscoTAC-1"
  active
  destination transport-method http
ntp server 10.254.0.10
!
!
!
!
!
!
restconf
end
 """