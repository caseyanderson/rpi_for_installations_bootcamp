## connectivity

In order to connect your development computer to the Raspberry Pi (to, say, test the fucntionality of something you just finished writing) one needs a few pieces of information:

1. a existing `username` on the Pi (all Raspberry Pis ship with a `pi` user)
2. password for `username` (all Raspberry Pis ship with `raspberry` as the password for the `pi` user, though we will use `adventures` instead)
3. an [IP Address](https://en.wikipedia.org/wiki/IP_address) or [hostname](https://en.wikipedia.org/wiki/Hostname)

Similarly, **the development computer must be on the same WiFi network as the Raspberry PI**.

## ssh

### connecting over ssh with a hostname shortcut

Open up a terminal, modify the following command to suit your needs, and then hit `[enter]`:

`ssh pi@raspberry.local`

In the above command I tell my development computer to look  for a device whose hostname is `raspberry` on the WiFi network I am already connected to (which we will refer to as the `local`). As long as the device is actually connected to the WiFi network, and my login credentials are correct, I should easily be able to connect to the device.

In order to avoid confusion between devices, I generally add a number to the end of the hostname so that multiple people can use this shortcut to reliably connect to specific devices on the same network. For example, for this workshop you will need to modify the example command above to something like the following:

`ssh pi@deploy1.local`

### connecting over ssh with an IP Address

If the hostname shortcut doesn't work, you can still connect to the device provided you **already know the IP Address** for the device. Though there are **lots** of different approaches to finding this information from a different computer, the simplest is to use the demo version of [this](https://www.iwaxx.com/lanscan/) tool.

Once you have located the IP Address, modify your code to resemble the below:

`ssh pi@10.4.26.38`

Which effectively accomplishes the **same thing** as the `hostname.local` method. It's tempting to convince yourself that `hostname.local` will **always** work in **all situations** but weird stuff happens from time to time in Linux-land, so being aware of alternative methods for common tasks is important.

## scp

The information necessary to connect
