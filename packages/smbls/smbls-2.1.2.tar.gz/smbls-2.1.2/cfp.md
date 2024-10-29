smbls: A Useful Tool for SMB Reconnaissance

---

SMB (Windows file shares, also interoperable with CIFS and Samba) is a network protocol with a variety security-relevant functionality on an enterprise network.

In this talk, we will give examples of common pentest/red team reconnaissance tasks that can be accomplished using the SMB protocol. Even if you're familiar with SMB, there might be more than you think! We will introduce `smbls`, an open source tool that can accomplish those tasks quickly and ergonomically.

Then we will talk about SMB permissions and dive progressively deeper into the SMB protocol. smbls even exposes one particular piece of permission information that is ignored by all common pentest tools.

If this talk is successful, you will try using smbls yourself. If it is really successful, you will also be inspired to write and publish your own multi-tool for another network protocol.

---


for target audience:
sysadmins/network defenders --


main takeaway: SMB is an interesting protocol with a variety security-relevant functionality on an enterprise network. smbls is a tool that can exercise that functionality at scale.

Followup: if SMB, one of the most well-known Windows protocols, has this much unexplored utility, what about other protocols?
