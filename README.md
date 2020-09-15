def update_sharing_info

Function calls UpdateDocumentSharingInfo

Microsoft documentation:
Link:
https://docs.microsoft.com/en-us/openspecs/sharepoint_protocols/ms-csomspt/fad1d6ca-77e9-42fa-93b3-73d7747fce18?redirectedfrom=MSDN

Text:
3.2.5.187.2.1.1 UpdateDocumentSharingInfo

    02/14/2019
    2 minutes to read

This method is a static CSOM method.

Return Type: CSOM array of Microsoft.SharePoint.Client.Sharing.UserSharingResult

This method allows a caller with the 'ManagePermission' permission to update sharing information about a document to enable document sharing with a set of users. It returns an array of UserSharingResult (section 3.2.5.190) elements where each element contains the sharing status for each user.

Parameters:

resourceAddress: A URL that points to a securable object, which can be a document, folder or the root folder of a document library.

Type: CSOM String

userRoleAssignments: An array of recipients and assigned roles on the securable object pointed to by the resourceAddress parameter.

Type: CSOM array of Microsoft.SharePoint.Client.Sharing.UserRoleAssignment

validateExistingPermissions: A Boolean flag indicating how to honor a requested permission for a user. If this value is "true", the protocol server will not grant the requested permission if a user already has sufficient permissions, and if this value is "false", the protocol server will grant the requested permission whether or not a user already has the same or more permissions. This parameter is applicable only when the parameter additiveMode is set to true.

Type: CSOM Boolean

additiveMode: A Boolean flag indicating whether the permission setting uses the additive or strict mode. If this value is "true", the permission setting uses the additive mode, which means that the specified permission will be added to the user's current list of permissions if it is not there already, and if this value is "false", the permission setting uses the strict mode, which means that the specified permission will replace the user's current permissions.

Type: CSOM Boolean

sendServerManagedNotification: A Boolean flag to indicate whether or not to generate an email notification to each recipient in the "userRoleAssignments" array after the document update is completed successfully. If this value is "true", the protocol server will send an email notification if an email server is configured, and if the value is "false", no email notification will be sent.

Type: CSOM Boolean

customMessage: A custom message to be included in the email notification.

Type: CSOM String

includeAnonymousLinksInNotification: A Boolean flag that indicates whether or not to include anonymous access links in the email notification to each recipient in the userRoleAssignments array after the document update is completed successfully. If the value is "true", the protocol server will include an anonymous access link in the email notification, and if the value is "false", no link will be included.

Type: CSOM Boolean

propagateAcl: A flag to determine if permissions SHOULD be pushed to items with unique permission.

Type: CSOM Boolean

__________________________________________
javascript example:
Link:
http://sharepointfieldnotes.blogspot.com/2014/09/sharing-documents-with-sharepoint-rest.html

Text:
function shareDocument()
{
    var hostweburl = decodeURIComponent(getQueryStringParameter('SPHostUrl'));
    var appweburl = decodeURIComponent(getQueryStringParameter('SPAppWebUrl'));
    var restSource = appweburl + "/_api/SP.Sharing.DocumentSharingManager.UpdateDocumentSharingInfo";


    $.ajax(
    {
        'url': restSource,
        'method': 'POST',
        'data': JSON.stringify({
            'resourceAddress': 'http://basesmc15/Shared%20Documents/A1210251607172880165.pdf',
            'userRoleAssignments': [{
                '__metadata': {
                    'type': 'SP.Sharing.UserRoleAssignment'
                },
                'Role': 1,
                'UserId': 'Chris Tester'
            }],
            'validateExistingPermissions': false,
            'additiveMode': true,
            'sendServerManagedNotification': false,
            'customMessage': "Please look at the following document",
            'includeAnonymousLinksInNotification': false
        }),
        'headers': {
            'accept': 'application/json;odata=verbose',
            'content-type': 'application/json;odata=verbose',
            'X-RequestDigest': $('#__REQUESTDIGEST').val()
        },
        'success': function (data) {
            var d = data;
        },
        'error': function (err) {
            alert(JSON.stringify(err));
        }
    }
    );

}

where roles could be assign by user role or name [or email]:

'userRoleAssignments': [{
                '__metadata': {
                    'type': 'SP.Sharing.UserRoleAssignment'
                },
                'Role': 1,
                'UserId': 'Translation Managers'
            },
            {
                '__metadata': {
                    'type': 'SP.Sharing.UserRoleAssignment'
                },
                'Role': 1,
                'UserId': 'Steve Tester'
            }]
