# tweetzotero

tweetzotero is a python automation script to save papers from twitter bookmarks to Zotero. It takes a csv file with tweet status URLs as input, fetch all the external URLs from those tweets, and save the papers to Zotero.

Prerequisites
----
Here's the things that needs to be done before running the script:
1. Get your Twitter `API Key`, `API Secret`, `Access Token` and `Access Secret` from [here](https://developer.twitter.com/en/portal/dashboard).
2. Set your default browser to `Google Chrome`. This script will work on this browser for now.
3. Export your twitter bookmark URLs as `csv` with the chrome extension [Dewey](https://chrome.google.com/webstore/detail/dewey/occohfgiljdagdmklhpplgmcnliljmgi).
4. Add Zotero extension to Google Chrome from [here](https://chrome.google.com/webstore/detail/zotero-connector/ekhagklcjbdpajgpjgmbionohlpdbjgc?hl=en). Also, install the Zotero software itself to your system. While running the script, the zotero app must be running.
5. `tweetzotero` uses the shortcut `ctrl/cmd + shift + s` on chrome to add the paper to zotero. So, make sure this shortcut actually works on chrome before running the script.
6. Make sure you have `conda` installed. If not, then install from [here](https://docs.conda.io/en/latest/miniconda.html).

Setup
----

Here's how you can download the code and setup environments:
```sh
git clone https://github.com/nahid18/tweetzotero.git
cd tweetzotero
conda create --name tweetzotero --file requirements.txt -y
conda activate tweetzotero
```
**Now, paste all 4 twitter keys to the `keys.py` file.**<br/><br/>
After that, you can run the script like below.

Usage
----

Once you have completed everything above, here's how you can run the script:
```sh
python tweetzotero.py -i <dewey-csv-file-path>
```
Example:
```sh
python tweetzotero.py -i example.csv
```
After running the script, just let the script complete tasks and don't do anything on your PC. <br/><br/>
For Help,
```sh
python tweetzotero.py -h
```

Inspiration
----
The inspiration of this project came from [here](https://twitter.com/RiyueSunnyBao/status/1404126160167055361).

Issues & Bugs
----
There could be many issues and bugs. Please report the issues and I'll try to resolve those.

License
----

MIT
