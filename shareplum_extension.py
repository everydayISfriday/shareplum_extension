from shareplum.site import Version, _Site2007, _Site365
from shareplum.folder import _Folder


class _Site365Extended(_Site365):

    def Folder(self, folder_name):
        """Sharepoint Folder Web Service
        """
        return _FolderExtended(self._session, folder_name, self.site_url)


class _FolderExtended(_Folder):

    def update_sharing_info(self, f_name, users_list,
                            validate_existing_permissions=False,
                            additive_mode=False, send_server_managed_notification=False,
                            custom_message=None, include_anonymous_links_in_notification=False):
        """
        Changes permission to Sharepoint resource: file or whole folder.
        Sample call: update_sharing_info('your_file_name', [{'Role': 1, 'Email': 'john.doe@company.com'}])
        :param f_name: (str)
                           file or folder name
        :param users_list: ([{}])
                           users whose permission will be changed ex. [{'Role': 1, 'Email': 'john.doe@company.com'}]
                           Available roles:
                           0 - None
                           1 - View
                           2 - Edit
                           3 - Owner
        :param validate_existing_permissions: (bool)
                           A Boolean flag indicating how to honor a requested permission for a user.
                           If this value is "true", the protocol server will not grant the requested permission
                           if a user already has sufficient permissions, and if this value is "false",
                           the protocol server will grant the requested permission whether or not
                           a user already has the same or more permissions.
                           This parameter is applicable only when the parameter additiveMode is set to true.
        :param additive_mode: (bool)
                           A Boolean flag indicating whether the permission setting uses the additive or strict mode.
                           If this value is "true", the permission setting uses the additive mode,
                           which means that the specified permission will be added to the user's current list of permissions
                           if it is not there already, and if this value is "false", the permission setting uses the strict mode,
                           which means that the specified permission will replace the user's current permissions.
        :param send_server_managed_notification: (bool)
                           A Boolean flag to indicate whether or not to generate an email notification to each recipient
                           in the "userRoleAssignments" array after the document update is completed successfully.
                           If this value is "true", the protocol server will send an email notification if
                           an email server is configured, and if the value is "false", no email notification will be sent.
        :param custom_message: (str)
                           A custom message to be included in the email notification.
        :param include_anonymous_links_in_notification: (bool)
                          A Boolean flag that indicates whether or not to include anonymous access links in the email
                          notification to each recipient in the userRoleAssignments array after the document update is
                          completed successfully. If the value is "true", the protocol server will include an anonymous
                          access link in the email notification, and if the value is "false", no link will be included.
        :return: response text
        """

        users = []
        for user in users_list:
            user_template = {'__metadata': {
                'type': 'SP.Sharing.UserRoleAssignment'
            }, 'Role': user.get('Role', None), 'UserId': user.get('Email', None)}

            users.append(user_template)

        url = self.site_url + f"/_api/SP.Sharing.DocumentSharingManager.UpdateDocumentSharingInfo"
        headers = {'accept': 'application/json;odata=verbose',
                   'content-type': 'application/json;odata=verbose',
                   'X-RequestDigest': self.contextinfo['FormDigestValue']}

        body = {
            'resourceAddress': self.site_url + f"{self.info['d']['Name']}/{f_name}",
            'userRoleAssignments': users,
            'validateExistingPermissions': validate_existing_permissions,
            'additiveMode': additive_mode,
            'sendServerManagedNotification': send_server_managed_notification,
            'customMessage': custom_message or "Please look at the following document",
            'includeAnonymousLinksInNotification': include_anonymous_links_in_notification
        }

        response = self._session.post(url=url,
                                      headers=headers,
                                      json=body)
        return response.text

    def get_file_response(self, file_name):
        """
        Returns whole response object. To return response.text use: get_file
        :param file_name: (str)
                Sharepoint file name
        :return: response object
        """
        response = self._session.get(
            self.site_url + f"/_api/web/GetFileByServerRelativeUrl('{self.info['d']['ServerRelativeUrl']}/{file_name}')/$value")

        return response


def SiteExtended(
        site_url,  # type: str
        version=Version.v2007,
        auth=None,  # type: Optional[Any]
        authcookie=None,  # type: Optional[requests.cookies.RequestsCookieJar]
        verify_ssl=True,  # type: bool
        ssl_version=None,  # type: Optional[float]
        huge_tree=False,  # type: bool
        timeout=None,  # type: Optional[int]
):

    # We ask for the various versions of SharePoint with 2010 as default
    # Multiple Version are allowed, but only 2010, 2013, and 365 are implemented
    if version == Version.v2007:
        return _Site2007(site_url,
                         auth,
                         authcookie,
                         verify_ssl,
                         ssl_version,
                         huge_tree,
                         timeout)

    elif version == Version.v2010:
        return _Site2007(site_url,
                         auth,
                         authcookie,
                         verify_ssl,
                         ssl_version,
                         huge_tree,
                         timeout)

    elif version == Version.v2013:
        return _Site365Extended(site_url,
                        auth,
                        authcookie,
                        verify_ssl,
                        ssl_version,
                        huge_tree,
                        timeout)

    elif version == Version.v2016:
        return _Site365Extended(site_url,
                        auth,
                        authcookie,
                        verify_ssl,
                        ssl_version,
                        huge_tree,
                        timeout)

    elif version == Version.v2019:
        return _Site365Extended(site_url,
                        auth,
                        authcookie,
                        verify_ssl,
                        ssl_version,
                        huge_tree,
                        timeout)

    elif version == Version.v365:
        return _Site365Extended(site_url,
                        auth,
                        authcookie,
                        verify_ssl,
                        ssl_version,
                        huge_tree,
                        timeout)