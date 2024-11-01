help([==[

Description
===========
unimelb-mf-clients is a collection of command-line tools to transfer data to/from Mediaflux, the data management platform operated by Research Computing Services.

More information
================
 - Homepage: https://unimelb.atlassian.net/wiki/spaces/RCS/pages/191037756/Mediaflux+Unimelb+Command-Line+Clients
]==])

whatis([==[Description: unimelb-mf-clients is a collection of command-line tools to transfer data to/from Mediaflux, the data management platform operated by Research Computing Services.]==])
whatis([==[Homepage: https://unimelb.atlassian.net/wiki/spaces/RCS/pages/191037756/Mediaflux+Unimelb+Command-Line+Clients]==])

local root = "/data/cephfs/unimelb-mf-clients/current/"

conflict("unimelb-mf-clients")

if not isloaded("Java/1.8.0_152") then
    load("Java/1.8.0_152")
end

prepend_path("PATH", pathJoin(root, "bin/unix"))

