<?xml version="1.0" encoding="UTF-8"?>

<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:template match="/">
  <html>
  <body bgcolor="d5d5d5" align="center">
  <h2>Employee Details</h2>
  <table border="1" padding="25%">
    <tr bgcolor="#0000f1" color='ffffff'>
      <th>Employee ID</th>
      <th>Employee Name</th>
      <th>Employee Salary</th>
      <th>Employee Designation</th>
    </tr>
    <xsl:for-each select="emp/employee">
    <tr>
      <td><xsl:value-of select="ID"/></td>
      <td><xsl:value-of select="Name"/></td>
      <td><xsl:value-of select="sal"/></td>
      <td><xsl:value-of select="des"/></td>
    </tr>
    </xsl:for-each>
  </table>
  </body>
  </html>
</xsl:template>

</xsl:stylesheet> 