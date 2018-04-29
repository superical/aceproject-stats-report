def emailHtmlBody(emailData):
    if emailData['hideEffortChart'] is False:
        emailData['effortChartHtml'] = getEffortChartHtml(emailData)
    else:
        emailData['effortChartHtml'] = ''

    emailHtmlBody = """
    <body style="background-color:#d7dde5;">


  <div style="background-color:#d7dde5;">

    <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
      <tbody>
        <tr>
          <td>


            <!--[if mso | IE]>
      <table
         align="center" border="0" cellpadding="0" cellspacing="0" style="width:1000px;" width="1000"
      >
        <tr>
          <td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;">
      <![endif]-->


            <div style="Margin:0px auto;max-width:1000px;">

              <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
                <tbody>
                  <tr>
                    <td style="direction:ltr;font-size:0px;padding:20px 0;text-align:center;vertical-align:top;">
                      <!--[if mso | IE]>
                  <table role="presentation" border="0" cellpadding="0" cellspacing="0">
                
        <tr>
      
            <td
               style="vertical-align:middle;width:666.6666666666665px;"
            >
          <![endif]-->

                      <div class="mj-column-per-66 outlook-group-fix" style="font-size:13px;text-align:left;direction:ltr;display:inline-block;vertical-align:middle;width:100%;">

                        <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:middle;" width="100%">

                          <tr>
                            <td align="left" style="font-size:0px;padding:10px 25px;padding-top:0;padding-bottom:0px;word-break:break-word;">

                              <div style="font-family:Ubuntu, Helvetica, Arial, sans-serif;font-size:11px;line-height:1;text-align:left;color:#000000;">
                                <span style="font-size: 11px">{data[projectName]} - {data[currentDateTime]:%d %b %Y, %I:%M %p}</span>
                              </div>

                            </td>
                          </tr>

                        </table>

                      </div>

                      <!--[if mso | IE]>
            </td>
          
            <td
               style="vertical-align:middle;width:333.33333333333326px;"
            >
          <![endif]-->

                      <div class="mj-column-per-33 outlook-group-fix" style="font-size:13px;text-align:left;direction:ltr;display:inline-block;vertical-align:middle;width:100%;">

                        <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:middle;" width="100%">

                          <tr>
                            <td align="right" style="font-size:0px;padding:10px 25px;padding-top:0;padding-bottom:0px;word-break:break-word;">

                              <div style="font-family:Ubuntu, Helvetica, Arial, sans-serif;font-size:11px;line-height:1;text-align:right;color:#000000;">
                                <span style="font-size: 11px">&#xA0;</span>
                              </div>

                            </td>
                          </tr>

                        </table>

                      </div>

                      <!--[if mso | IE]>
            </td>
          
        </tr>
      
                  </table>
                <![endif]-->
                    </td>
                  </tr>
                </tbody>
              </table>

            </div>


            <!--[if mso | IE]>
          </td>
        </tr>
      </table>
      <![endif]-->


          </td>
        </tr>
      </tbody>
    </table>

    <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="background:#e85034;background-color:#e85034;width:100%;">
      <tbody>
        <tr>
          <td>


            <!--[if mso | IE]>
      <table
         align="center" border="0" cellpadding="0" cellspacing="0" style="width:1000px;" width="1000"
      >
        <tr>
          <td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;">
      <![endif]-->


            <div style="Margin:0px auto;max-width:1000px;">

              <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
                <tbody>
                  <tr>
                    <td style="direction:ltr;font-size:0px;padding:20px 0;text-align:center;vertical-align:top;">
                      <!--[if mso | IE]>
                  <table role="presentation" border="0" cellpadding="0" cellspacing="0">
                
        <tr>
      
            <td
               style="vertical-align:middle;width:1000px;"
            >
          <![endif]-->

                      <div class="mj-column-per-100 outlook-group-fix" style="font-size:13px;text-align:left;direction:ltr;display:inline-block;vertical-align:middle;width:100%;">

                        <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:middle;" width="100%">

                          <tr>
                            <td align="left" style="font-size:0px;padding:0 20px;word-break:break-word;">

                              <div style="font-family:Ubuntu, Arial, Helvetica, sans-serif;font-size:26px;line-height:40px;text-align:left;color:ffffff;">
                                <span style="color:#ffffff">Project Tasks Overview</span>
                              </div>

                            </td>
                          </tr>

                          <tr>
                            <td align="left" style="font-size:0px;padding:0 20px;word-break:break-word;">

                              <div style="font-family:Ubuntu, Helvetica, Arial, sans-serif;font-size:13px;line-height:1;text-align:left;color:#e5e5e5;">
                                <span style="font-size: 20px; font-style:normal; font-weight: 100; font-family:Ubuntu, Arial,Helvetica, sans-serif">{data[projectName]}</span>
                              </div>

                            </td>
                          </tr>

                        </table>

                      </div>

                      <!--[if mso | IE]>
            </td>
          
        </tr>
      
                  </table>
                <![endif]-->
                    </td>
                  </tr>
                </tbody>
              </table>

            </div>


            <!--[if mso | IE]>
          </td>
        </tr>
      </table>
      <![endif]-->


          </td>
        </tr>
      </tbody>
    </table>

    <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="background:#ffffff;background-color:#ffffff;width:100%;">
      <tbody>
        <tr>
          <td>


            <!--[if mso | IE]>
      <table
         align="center" border="0" cellpadding="0" cellspacing="0" style="width:1000px;" width="1000"
      >
        <tr>
          <td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;">
      <![endif]-->


            <div style="Margin:0px auto;max-width:1000px;">

              <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
                <tbody>
                  <tr>
                    <td style="direction:ltr;font-size:0px;padding:20px 0;text-align:center;vertical-align:middle;">
                      <!--[if mso | IE]>
                  <table role="presentation" border="0" cellpadding="0" cellspacing="0">
                
        <tr>
      
            <td
               style="vertical-align:middle;width:1000px;"
            >
          <![endif]-->

                      <div class="mj-column-per-100 outlook-group-fix" style="font-size:13px;text-align:left;direction:ltr;display:inline-block;vertical-align:middle;width:100%;">

                        <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:middle;" width="100%">

                          <tr>
                            <td align="center" style="font-size:0px;padding:10px 25px;padding-top:5;padding-bottom:5px;word-break:break-word;">

                              <div style="font-family:Ubuntu, Helvetica, Arial, sans-serif;font-size:14px;line-height:28px;text-align:center;color:#45474e;">
                                <span style="font-size: 26px; line-height: 34px;">Gantt Chart</span>
                                <br>
                                <span style="color: #e85034; font-size:12px">Tasks from {data[ganttChartStartEndDate][0]:%d %b %Y} to {data[ganttChartStartEndDate][1]:%d %b %Y}</span>
                              </div>

                            </td>
                          </tr>

                          <tr>
                            <td align="center" style="font-size:0px;padding:0px;word-break:break-word;">

                              <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-collapse:collapse;border-spacing:0px;">
                                <tbody>
                                  <tr>
                                    <td style="width:1000px;">

                                      <img height="auto" src="cid:{data[cidGanttChart]}" style="border:none;display:block;outline:none;text-decoration:none;width:100%;" width="1000" />

                                    </td>
                                  </tr>
                                </tbody>
                              </table>

                            </td>
                          </tr>

                        </table>

                      </div>

                      <!--[if mso | IE]>
            </td>
          
        </tr>
      
                  </table>
                <![endif]-->
                    </td>
                  </tr>
                </tbody>
              </table>

            </div>


            <!--[if mso | IE]>
          </td>
        </tr>
      </table>
      <![endif]-->


          </td>
        </tr>
      </tbody>
    </table>

    {data[effortChartHtml]}

    <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="background:#FFFFFF;background-color:#FFFFFF;width:100%;">
      <tbody>
        <tr>
          <td>


            <!--[if mso | IE]>
      <table
         align="center" border="0" cellpadding="0" cellspacing="0" style="width:1000px;" width="1000"
      >
        <tr>
          <td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;">
      <![endif]-->


            <div style="Margin:0px auto;max-width:1000px;">

              <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
                <tbody>
                  <tr>
                    <td style="direction:ltr;font-size:0px;padding:20px 0;padding-top:10px;text-align:center;vertical-align:top;">
                      <!--[if mso | IE]>
                  <table role="presentation" border="0" cellpadding="0" cellspacing="0">
                
        <tr>
      
            <td
               style="vertical-align:top;width:1000px;"
            >
          <![endif]-->

                      <div class="mj-column-per-100 outlook-group-fix" style="font-size:13px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">

                        <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:top;" width="100%">

                          <tr>
                            <td align="center" style="font-size:0px;padding:10px 25px;word-break:break-word;">

                              <div style="font-family:Ubuntu, Helvetica, Arial, sans-serif;font-size:13px;line-height:1;text-align:center;color:#000000;">
                                <strong><span style="font-size: 40px; color:#e85034">––</span></strong>
                              </div>

                            </td>
                          </tr>

                        </table>

                      </div>

                      <!--[if mso | IE]>
            </td>
          
        </tr>
      
                  </table>
                <![endif]-->
                    </td>
                  </tr>
                </tbody>
              </table>

            </div>


            <!--[if mso | IE]>
          </td>
        </tr>
      </table>
      <![endif]-->


          </td>
        </tr>
      </tbody>
    </table>

    <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="background:#ffffff;background-color:#ffffff;width:100%;">
      <tbody>
        <tr>
          <td>


            <!--[if mso | IE]>
      <table
         align="center" border="0" cellpadding="0" cellspacing="0" style="width:1000px;" width="1000"
      >
        <tr>
          <td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;">
      <![endif]-->


            <div style="Margin:0px auto;max-width:1000px;">

              <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
                <tbody>
                  <tr>
                    <td style="direction:ltr;font-size:0px;padding:20px 0;text-align:center;vertical-align:middle;">
                      <!--[if mso | IE]>
                  <table role="presentation" border="0" cellpadding="0" cellspacing="0">
                
        <tr>
      
            <td
               style="vertical-align:middle;width:1000px;"
            >
          <![endif]-->

                      <div class="mj-column-per-100 outlook-group-fix" style="font-size:13px;text-align:left;direction:ltr;display:inline-block;vertical-align:middle;width:100%;">

                        <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:middle;" width="100%">

                          <tr>
                            <td align="center" style="font-size:0px;padding:10px 25px;padding-top:0;padding-bottom:0px;word-break:break-word;">

                              <div style="font-family:Ubuntu, Helvetica, Arial, sans-serif;font-size:14px;line-height:28px;text-align:center;color:#45474e;">
                                <span style="font-size: 26px; line-height: 34px;">At a Glance</span>
                                <br>
                                <span style="color: #e85034; font-size:12px">Other stats about the project</span>
                              </div>

                            </td>
                          </tr>

                        </table>

                      </div>

                      <!--[if mso | IE]>
            </td>
          
        </tr>
      
                  </table>
                <![endif]-->
                    </td>
                  </tr>
                </tbody>
              </table>

            </div>


            <!--[if mso | IE]>
          </td>
        </tr>
      </table>
      <![endif]-->


          </td>
        </tr>
      </tbody>
    </table>

    <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="background:#ffffff;background-color:#ffffff;width:100%;">
      <tbody>
        <tr>
          <td>


            <!--[if mso | IE]>
      <table
         align="center" border="0" cellpadding="0" cellspacing="0" style="width:1000px;" width="1000"
      >
        <tr>
          <td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;">
      <![endif]-->


            <div style="Margin:0px auto;max-width:1000px;">

              <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
                <tbody>
                  <tr>
                    <td style="direction:ltr;font-size:0px;padding:20px 0;padding-top:0;text-align:center;vertical-align:top;">
                      <!--[if mso | IE]>
                  <table role="presentation" border="0" cellpadding="0" cellspacing="0">
                
        <tr>
      
            <td
               style="vertical-align:top;width:500px;"
            >
          <![endif]-->

                      <div class="mj-column-per-50 outlook-group-fix" style="font-size:13px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">

                        <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:top;" width="100%">

                          <tr>
                            <td align="center" style="font-size:0px;padding:10px 25px;padding-top:0;padding-bottom:0px;word-break:break-word;">

                              <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-collapse:collapse;border-spacing:0px;">
                                <tbody>
                                  <tr>
                                    <td style="width:450px;">

                                      <img height="auto" src="cid:{data[cidStatusPriorityPlot]}" style="border:0;display:block;outline:none;text-decoration:none;width:100%;" width="450" />

                                    </td>
                                  </tr>
                                </tbody>
                              </table>

                            </td>
                          </tr>

                          <tr>
                            <td align="center" style="font-size:0px;padding:10px 25px;padding-top:10;padding-bottom:30px;word-break:break-word;">

                              <div style="font-family:Ubuntu, Helvetica, Arial, sans-serif;font-size:11px;line-height:1.5;text-align:center;color:#9da3a3;">
                                <span style="font-size: 14px; color: #e85034">Task Status/Priority Breakdown</span><br>Breakdown of task statuses and their number of corresponding tasks and priorities as at {data[currentDateTime]:%d %b %Y %I:%M %p}.
                              </div>

                            </td>
                          </tr>

                        </table>

                      </div>

                      <!--[if mso | IE]>
            </td>
          
            <td
               style="vertical-align:top;width:500px;"
            >
          <![endif]-->

                      <div class="mj-column-per-50 outlook-group-fix" style="font-size:13px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">

                        <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:top;" width="100%">

                          <tr>
                            <td align="center" style="font-size:0px;padding:10px 25px;padding-top:0;padding-bottom:0px;word-break:break-word;">

                              <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-collapse:collapse;border-spacing:0px;">
                                <tbody>
                                  <tr>
                                    <td style="width:450px;">

                                      <img height="auto" src="cid:{data[cidPriorityCountPlot]}" style="border:0;display:block;outline:none;text-decoration:none;width:100%;" width="450" />

                                    </td>
                                  </tr>
                                </tbody>
                              </table>

                            </td>
                          </tr>

                          <tr>
                            <td align="center" style="font-size:0px;padding:10px 25px;padding-top:10;padding-bottom:30px;word-break:break-word;">

                              <div style="font-family:Ubuntu, Helvetica, Arial, sans-serif;font-size:11px;line-height:1.5;text-align:center;color:#9da3a3;">
                                <span style="font-size: 14px; color: #e85034">Task Priority Count</span><br>Number of tasks of different priorities created in the last {data[priorityCountChartStartEndDate][2].days} days.
                              </div>

                            </td>
                          </tr>

                        </table>

                      </div>

                      <!--[if mso | IE]>
            </td>
          
        </tr>
      
                  </table>
                <![endif]-->
                    </td>
                  </tr>
                </tbody>
              </table>

            </div>


            <!--[if mso | IE]>
          </td>
        </tr>
      </table>
      <![endif]-->


          </td>
        </tr>
      </tbody>
    </table>

    <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="background:#ffffff;background-color:#ffffff;width:100%;">
      <tbody>
        <tr>
          <td>


            <!--[if mso | IE]>
      <table
         align="center" border="0" cellpadding="0" cellspacing="0" style="width:1000px;" width="1000"
      >
        <tr>
          <td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;">
      <![endif]-->


            <div style="Margin:0px auto;max-width:1000px;">

              <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
                <tbody>
                  <tr>
                    <td style="direction:ltr;font-size:0px;padding:20px 0;padding-top:0;text-align:center;vertical-align:top;">
                      <!--[if mso | IE]>
                  <table role="presentation" border="0" cellpadding="0" cellspacing="0">
                
        <tr>
      
            <td
               style="vertical-align:top;width:500px;"
            >
          <![endif]-->

                      <div class="mj-column-per-50 outlook-group-fix" style="font-size:13px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">

                        <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:top;" width="100%">

                          <tr>
                            <td align="center" style="font-size:0px;padding:10px 25px;padding-top:0;padding-bottom:0px;word-break:break-word;">

                              <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-collapse:collapse;border-spacing:0px;">
                                <tbody>
                                  <tr>
                                    <td style="width:450px;">

                                      <img height="auto" src="cid:{data[cidDaysTakenPlot]}" style="border:0;display:block;outline:none;text-decoration:none;width:100%;" width="450" />

                                    </td>
                                  </tr>
                                </tbody>
                              </table>

                            </td>
                          </tr>

                          <tr>
                            <td align="center" style="font-size:0px;padding:10px 25px;padding-top:10;padding-bottom:30px;word-break:break-word;">

                              <div style="font-family:Ubuntu, Helvetica, Arial, sans-serif;font-size:11px;line-height:1.5;text-align:center;color:#9da3a3;">
                                <span style="font-size: 14px; color: #e85034">Days Taken to Complete Tasks</span><br>Number of days taken to complete tasks of different priorities in the last {data[priorityDaysTakenStartEndDate][2].days} days.
                              </div>

                            </td>
                          </tr>

                        </table>

                      </div>

                      <!--[if mso | IE]>
            </td>
          
            <td
               style="vertical-align:top;width:500px;"
            >
          <![endif]-->

                      <div class="mj-column-per-50 outlook-group-fix" style="font-size:13px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">

                        <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:top;" width="100%">

                          <tr>
                            <td align="center" style="font-size:0px;padding:10px 25px;padding-top:0;padding-bottom:0px;word-break:break-word;">

                              <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-collapse:collapse;border-spacing:0px;">
                                <tbody>
                                  <tr>
                                    <td style="width:450px;">

                                      <img height="auto" src="cid:{data[cidDayCreatedPlot]}" style="border:0;display:block;outline:none;text-decoration:none;width:100%;" width="450" />

                                    </td>
                                  </tr>
                                </tbody>
                              </table>

                            </td>
                          </tr>

                          <tr>
                            <td align="center" style="font-size:0px;padding:10px 25px;padding-top:10;padding-bottom:30px;word-break:break-word;">

                              <div style="font-family:Ubuntu, Helvetica, Arial, sans-serif;font-size:11px;line-height:1.5;text-align:center;color:#9da3a3;">
                                <span style="font-size: 14px; color: #e85034">Tasks Created on Days</span><br>Number of tasks created on day of week in the last {data[tasksCreatedOnDayStartEndDate][2].days} days.
                              </div>

                            </td>
                          </tr>

                        </table>

                      </div>

                      <!--[if mso | IE]>
            </td>
          
        </tr>
      
                  </table>
                <![endif]-->
                    </td>
                  </tr>
                </tbody>
              </table>

            </div>


            <!--[if mso | IE]>
          </td>
        </tr>
      </table>
      <![endif]-->


          </td>
        </tr>
      </tbody>
    </table>

    <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="background:#ffffff;background-color:#ffffff;width:100%;">
      <tbody>
        <tr>
          <td>


            <!--[if mso | IE]>
      <table
         align="center" border="0" cellpadding="0" cellspacing="0" style="width:1000px;" width="1000"
      >
        <tr>
          <td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;">
      <![endif]-->


            <div style="Margin:0px auto;max-width:1000px;">

              <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
                <tbody>
                  <tr>
                    <td style="direction:ltr;font-size:0px;padding:20px 0;padding-top:0;text-align:center;vertical-align:top;">
                      <!--[if mso | IE]>
                  <table role="presentation" border="0" cellpadding="0" cellspacing="0">
                
        <tr>
      
            <td
               style="vertical-align:top;width:1000px;"
            >
          <![endif]-->

                      <div class="mj-column-per-100 outlook-group-fix" style="font-size:13px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">

                        <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:top;" width="100%">

                          <tr>
                            <td align="center" style="font-size:0px;padding:10px 25px;padding-top:0;padding-bottom:0px;word-break:break-word;">

                              <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-collapse:collapse;border-spacing:0px;">
                                <tbody>
                                  <tr>
                                    <td style="width:950px;">

                                      <img height="auto" src="cid:{data[cidTasksWordcloud]}" style="border:0;display:block;outline:none;text-decoration:none;width:100%;" width="950" />

                                    </td>
                                  </tr>
                                </tbody>
                              </table>

                            </td>
                          </tr>

                          <tr>
                            <td align="center" style="font-size:0px;padding:10px 25px;padding-top:10;padding-bottom:30px;word-break:break-word;">

                              <div style="font-family:Ubuntu, Helvetica, Arial, sans-serif;font-size:11px;line-height:1.5;text-align:center;color:#9da3a3;">
                                <span style="font-size: 14px; color: #e85034">Topic Trend</span><br>Words and phrases mentioned in the last {data[tasksWordcloudStartEndDate][2].days} days.
                              </div>

                            </td>
                          </tr>

                        </table>

                      </div>

                      <!--[if mso | IE]>
            </td>
          
        </tr>
      
                  </table>
                <![endif]-->
                    </td>
                  </tr>
                </tbody>
              </table>

            </div>


            <!--[if mso | IE]>
          </td>
        </tr>
      </table>
      <![endif]-->


          </td>
        </tr>
      </tbody>
    </table>

    <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="background:#e85034;background-color:#e85034;width:100%;">
      <tbody>
        <tr>
          <td>


            <!--[if mso | IE]>
      <table
         align="center" border="0" cellpadding="0" cellspacing="0" style="width:1000px;" width="1000"
      >
        <tr>
          <td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;">
      <![endif]-->


            <div style="Margin:0px auto;max-width:1000px;">

              <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
                <tbody>
                  <tr>
                    <td style="direction:ltr;font-size:0px;padding:20px 0;text-align:center;vertical-align:middle;">
                      <!--[if mso | IE]>
                  <table role="presentation" border="0" cellpadding="0" cellspacing="0">
                
        <tr>
      
            <td
               style="vertical-align:middle;width:1000px;"
            >
          <![endif]-->

                      <div class="mj-column-per-100 outlook-group-fix" style="font-size:13px;text-align:left;direction:ltr;display:inline-block;vertical-align:middle;width:100%;">

                        <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:middle;" width="100%">

                          <tr>
                            <td align="center" style="font-size:0px;padding:10px 25px;padding-top:25;padding-bottom:10px;word-break:break-word;">

                              <div style="font-family:Ubuntu, Helvetica, Arial, sans-serif;font-size:20px;line-height:1;text-align:center;color:#ffffff;">
                                Summary
                              </div>

                            </td>
                          </tr>

                          <tr>
                            <td style="font-size:0px;padding:10px 25px;padding-top:20;padding-right:100px;padding-bottom:20px;padding-left:100px;word-break:break-word;">

                              <p style="border-top:solid 1px #fff;font-size:1;margin:0px auto;width:100%;">
                              </p>

                              <!--[if mso | IE]>
        <table
           align="center" border="0" cellpadding="0" cellspacing="0" style="border-top:solid 1px #fff;font-size:1;margin:0px auto;width:800px;" role="presentation" width="800px"
        >
          <tr>
            <td style="height:0;line-height:0;">
              &nbsp;
            </td>
          </tr>
        </table>
      <![endif]-->


                            </td>
                          </tr>

                          <tr>
                            <td align="center" style="font-size:0px;padding:10px 25px;padding-top:20;padding-bottom:25px;word-break:break-word;">

                              <div style="font-family:Ubuntu, Helvetica, Arial, sans-serif;font-size:12px;line-height:1.8;text-align:center;color:#f8d5d1;">
                                There is a total of {data[totalHeadCounts]} headcounts on this project. Considering that each work day consists of {data[effortPerDay]} hours, this amounts to a total available resource of {data[totalAvailableEffortResource]} efforts. The team is targeted
                                to perform at {data[expectedProficiency]:.1f}% proficiency level between {data[burndownChartStartEndDate][0]:%d %b %Y} and {data[burndownChartStartEndDate][1]:%d %b %Y}. Thus, the total ideal effort to burn is {data[expectedLinearEffortToBurn]:.1f}
                                efforts and the ideal effort burndown trend is {data[expectedEffortBurnVelocity]:.1f} efforts/day. Based on the targeted proficiency level, the team's actual effort burndown efficiency in this period is estimated to be
                                at {data[effortEfficiencyRating]:.2f}%.<br><br>
                              </div>

                            </td>
                          </tr>

                        </table>

                      </div>

                      <!--[if mso | IE]>
            </td>
          
        </tr>
      
                  </table>
                <![endif]-->
                    </td>
                  </tr>
                </tbody>
              </table>

            </div>


            <!--[if mso | IE]>
          </td>
        </tr>
      </table>
      <![endif]-->


          </td>
        </tr>
      </tbody>
    </table>

    <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
      <tbody>
        <tr>
          <td>


            <!--[if mso | IE]>
      <table
         align="center" border="0" cellpadding="0" cellspacing="0" style="width:1000px;" width="1000"
      >
        <tr>
          <td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;">
      <![endif]-->


            <div style="Margin:0px auto;max-width:1000px;">

              <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
                <tbody>
                  <tr>
                    <td style="direction:ltr;font-size:0px;padding:20px 0;text-align:center;vertical-align:top;">
                      <!--[if mso | IE]>
                  <table role="presentation" border="0" cellpadding="0" cellspacing="0">
                
        <tr>
      
            <td
               style="vertical-align:middle;width:1000px;"
            >
          <![endif]-->

                      <div class="mj-column-per-100 outlook-group-fix" style="font-size:13px;text-align:left;direction:ltr;display:inline-block;vertical-align:middle;width:100%;">

                        <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:middle;" width="100%">

                          <tr>
                            <td align="center" style="font-size:0px;padding:10px 25px;padding-top:0;padding-bottom:0px;word-break:break-word;">

                              <div style="font-family:Ubuntu, Helvetica, Arial, sans-serif;font-size:11px;line-height:1;text-align:center;color:#000000;">
                                <p style="font-size: 11px">Project data retrieved on {data[currentDateTime]:%d %b %Y at %I:%M %p}.</p>
                              </div>

                            </td>
                          </tr>

                          <tr>
                            <td align="center" style="font-size:0px;padding:10px 25px;padding-top:0;padding-bottom:0px;word-break:break-word;">

                              <div style="font-family:Ubuntu, Helvetica, Arial, sans-serif;font-size:11px;line-height:1;text-align:center;color:#000000;">
                                <p style="font-size: 11px">Seth's ACE Reporter - v{data[appVersion]}</p>
                              </div>

                            </td>
                          </tr>

                        </table>

                      </div>

                      <!--[if mso | IE]>
            </td>
          
        </tr>
      
                  </table>
                <![endif]-->
                    </td>
                  </tr>
                </tbody>
              </table>

            </div>


            <!--[if mso | IE]>
          </td>
        </tr>
      </table>
      <![endif]-->


          </td>
        </tr>
      </tbody>
    </table>

  </div>

</body>
    """.format(data=emailData).replace('\n','')
    return emailHtmlBody

def getEffortChartHtml(emailData):
    return """
        <!-- Start of Effort Chart -->
    <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="background:#FFFFFF;background-color:#FFFFFF;width:100%;">
      <tbody>
        <tr>
          <td>


            <!--[if mso | IE]>
      <table
         align="center" border="0" cellpadding="0" cellspacing="0" style="width:1000px;" width="1000"
      >
        <tr>
          <td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;">
      <![endif]-->


            <div style="Margin:0px auto;max-width:1000px;">

              <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
                <tbody>
                  <tr>
                    <td style="direction:ltr;font-size:0px;padding:20px 0;padding-top:0px;text-align:center;vertical-align:top;">
                      <!--[if mso | IE]>
                  <table role="presentation" border="0" cellpadding="0" cellspacing="0">
                
        <tr>
      
            <td
               style="vertical-align:top;width:1000px;"
            >
          <![endif]-->

                      <div class="mj-column-per-100 outlook-group-fix" style="font-size:13px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">

                        <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:top;" width="100%">

                          <tr>
                            <td align="center" style="font-size:0px;padding:10px 25px;word-break:break-word;">

                              <div style="font-family:Ubuntu, Helvetica, Arial, sans-serif;font-size:13px;line-height:1;text-align:center;color:#000000;">
                                <strong><span style="font-size: 40px; color:#e85034">––</span></strong>
                              </div>

                            </td>
                          </tr>

                        </table>

                      </div>

                      <!--[if mso | IE]>
            </td>
          
        </tr>
      
                  </table>
                <![endif]-->
                    </td>
                  </tr>
                </tbody>
              </table>

            </div>


            <!--[if mso | IE]>
          </td>
        </tr>
      </table>
      <![endif]-->


          </td>
        </tr>
      </tbody>
    </table>

    <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="background:#ffffff;background-color:#ffffff;width:100%;">
      <tbody>
        <tr>
          <td>


            <!--[if mso | IE]>
      <table
         align="center" border="0" cellpadding="0" cellspacing="0" style="width:1000px;" width="1000"
      >
        <tr>
          <td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;">
      <![endif]-->


            <div style="Margin:0px auto;max-width:1000px;">

              <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
                <tbody>
                  <tr>
                    <td style="direction:ltr;font-size:0px;padding:0px 0px;text-align:center;vertical-align:middle;">
                      <!--[if mso | IE]>
                  <table role="presentation" border="0" cellpadding="0" cellspacing="0">
                
        <tr>
      
            <td
               style="vertical-align:middle;width:1000px;"
            >
          <![endif]-->

                      <div class="mj-column-per-100 outlook-group-fix" style="font-size:13px;text-align:left;direction:ltr;display:inline-block;vertical-align:middle;width:100%;">

                        <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:middle;" width="100%">

                          <tr>
                            <td align="center" style="font-size:0px;padding:10px 25px;padding-top:0;padding-bottom:10px;word-break:break-word;">

                              <div style="font-family:Ubuntu, Helvetica, Arial, sans-serif;font-size:14px;line-height:28px;text-align:center;color:#45474e;">
                                <span style="font-size: 26px; line-height: 34px;">Effort Chart</span>
                                <br>
                                <span style="color: #e85034; font-size:12px">Effort burndown from {data[burndownChartStartEndDate][0]:%d %b %Y} to {data[burndownChartStartEndDate][1]:%d %b %Y, %I:%M %p}</span>
                                <br>
                                <span style="color: #e85034; font-size:12px; line-height:8px">Team proficiency targeted at {data[expectedProficiency]:.1f}%</span>
                              </div>

                            </td>
                          </tr>

                          <tr>
                            <td align="center" style="font-size:0px;padding:0px;word-break:break-word;">

                              <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-collapse:collapse;border-spacing:0px;">
                                <tbody>
                                  <tr>
                                    <td style="width:1000px;">

                                      <img height="auto" src="cid:{data[cidBurndown]}" style="border:none;display:block;outline:none;text-decoration:none;width:100%;" width="1000" />

                                    </td>
                                  </tr>
                                </tbody>
                              </table>

                            </td>
                          </tr>

                        </table>

                      </div>

                      <!--[if mso | IE]>
            </td>
          
        </tr>
      
                  </table>
                <![endif]-->
                    </td>
                  </tr>
                </tbody>
              </table>

            </div>


            <!--[if mso | IE]>
          </td>
        </tr>
      </table>
      <![endif]-->


          </td>
        </tr>
      </tbody>
    </table>

    <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="background:#ffffff;background-color:#ffffff;width:100%;">
      <tbody>
        <tr>
          <td>


            <!--[if mso | IE]>
      <table
         align="center" border="0" cellpadding="0" cellspacing="0" style="width:1000px;" width="1000"
      >
        <tr>
          <td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;">
      <![endif]-->


            <div style="Margin:0px auto;max-width:1000px;">

              <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
                <tbody>
                  <tr>
                    <td style="direction:ltr;font-size:0px;padding:0px 0px;text-align:center;vertical-align:middle;">
                      <!--[if mso | IE]>
                  <table role="presentation" border="0" cellpadding="0" cellspacing="0">
                
        <tr>
      
            <td
               style="vertical-align:middle;width:333.33333333333326px;"
            >
          <![endif]-->

                      <div class="mj-column-per-33 outlook-group-fix" style="font-size:13px;text-align:left;direction:ltr;display:inline-block;vertical-align:middle;width:100%;">

                        <table background="#FC9886" border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%">
                          <tbody>
                            <tr>
                              <td style="background-color:#FC9886;border:1px solid white;vertical-align:middle;padding:0px;">

                                <table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%">

                                  <tr>
                                    <td align="center" style="font-size:0px;padding:0px 0px;padding-top:18px;word-break:break-word;">

                                      <div style="font-family:Ubuntu, Helvetica, Arial, sans-serif;font-size:13px;line-height:1;text-align:center;color:#000000;">
                                        <br/> Total Efforts Burnt<br/><br/>
                                      </div>

                                    </td>
                                  </tr>

                                  <tr>
                                    <td align="center" style="font-size:0px;padding:0px 0px;word-break:break-word;">

                                      <div style="font-family:Ubuntu, Helvetica, Arial, sans-serif;font-size:36px;line-height:38px;text-align:center;color:#000000;">
                                        {data[totalEffortBurnt]}
                                      </div>

                                    </td>
                                  </tr>

                                  <tr>
                                    <td align="center" style="font-size:0px;padding:0px 0px;padding-bottom:35px;word-break:break-word;">

                                      <div style="font-family:Ubuntu, Helvetica, Arial, sans-serif;font-size:10px;line-height:12px;text-align:center;color:#000000;">
                                        effort hours
                                        <br/><br/>
                                      </div>

                                    </td>
                                  </tr>

                                </table>

                              </td>
                            </tr>
                          </tbody>
                        </table>

                      </div>

                      <!--[if mso | IE]>
            </td>
          
            <td
               style="vertical-align:middle;width:333.33333333333326px;"
            >
          <![endif]-->

                      <div class="mj-column-per-33 outlook-group-fix" style="font-size:13px;text-align:left;direction:ltr;display:inline-block;vertical-align:middle;width:100%;">

                        <table background="#8BE0BE" border="0" cellpadding="0" cellspacing="0" role="presentation" style="background-color:#8BE0BE;border:1px solid white;vertical-align:middle;" width="100%">

                          <tr>
                            <td align="center" style="font-size:0px;padding:0px 0px;padding-top:18px;word-break:break-word;">

                              <div style="font-family:Ubuntu, Helvetica, Arial, sans-serif;font-size:13px;line-height:1;text-align:center;color:#000000;">
                                <br/> Effort Burndown Trend<br/><br/>
                              </div>

                            </td>
                          </tr>

                          <tr>
                            <td align="center" style="font-size:0px;padding:0px 0px;word-break:break-word;">

                              <div style="font-family:Ubuntu, Helvetica, Arial, sans-serif;font-size:36px;line-height:38px;text-align:center;color:#000000;">
                                {data[effortBurnVelocity]:.1f}
                              </div>

                            </td>
                          </tr>

                          <tr>
                            <td align="center" style="font-size:0px;padding:0px 0px;padding-bottom:35px;word-break:break-word;">

                              <div style="font-family:Ubuntu, Helvetica, Arial, sans-serif;font-size:10px;line-height:12px;text-align:center;color:#000000;">
                                efforts / day
                                <br/><br/>
                              </div>

                            </td>
                          </tr>

                        </table>

                      </div>

                      <!--[if mso | IE]>
            </td>
          
            <td
               style="vertical-align:middle;width:333.33333333333326px;"
            >
          <![endif]-->

                      <div class="mj-column-per-33 outlook-group-fix" style="font-size:13px;text-align:left;direction:ltr;display:inline-block;vertical-align:middle;width:100%;">

                        <table background="#FDDDA2" border="0" cellpadding="0" cellspacing="0" role="presentation" style="background-color:#FDDDA2;border:1px solid white;vertical-align:middle;" width="100%">

                          <tr>
                            <td align="center" style="font-size:0px;padding:0px 0px;padding-top:18px;word-break:break-word;">

                              <div style="font-family:Ubuntu, Helvetica, Arial, sans-serif;font-size:13px;line-height:1;text-align:center;color:#000000;">
                                <br/> Avg. Effort Creation Rate<br/><br/>
                              </div>

                            </td>
                          </tr>

                          <tr>
                            <td align="center" style="font-size:0px;padding:0px 0px;word-break:break-word;">

                              <div style="font-family:Ubuntu, Helvetica, Arial, sans-serif;font-size:36px;line-height:38px;text-align:center;color:#000000;">
                                {data[effortCreationRate]:.1f}
                              </div>

                            </td>
                          </tr>

                          <tr>
                            <td align="center" style="font-size:0px;padding:0px 0px;padding-bottom:35px;word-break:break-word;">

                              <div style="font-family:Ubuntu, Helvetica, Arial, sans-serif;font-size:10px;line-height:12px;text-align:center;color:#000000;">
                                efforts / day
                                <br/><br/>
                              </div>

                            </td>
                          </tr>

                        </table>

                      </div>

                      <!--[if mso | IE]>
            </td>
          
        </tr>
      
                  </table>
                <![endif]-->
                    </td>
                  </tr>
                </tbody>
              </table>

            </div>


            <!--[if mso | IE]>
          </td>
        </tr>
      </table>
      <![endif]-->


          </td>
        </tr>
      </tbody>
    </table>
    <!-- End of Effort Chart -->
    """.format(data=emailData).replace('\n','')

def emailHtmlHeader():
    return """
    <!doctype html>
    <html xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">
    
    <head>
      <title></title>
      <!--[if !mso]><!-- -->
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <!--<![endif]-->
      <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
      <meta name="viewport" content="width=device-width,initial-scale=1">
      <style type="text/css">
        #outlook a {
          padding: 0
        }
    
        .ReadMsgBody {
          width: 100%
        }
    
        .ExternalClass {
          width: 100%
        }
    
        .ExternalClass * {
          line-height: 100%
        }
    
        body {
          margin: 0;
          padding: 0;
          -webkit-text-size-adjust: 100%;
          -ms-text-size-adjust: 100%
        }
    
        table,
        td {
          border-collapse: collapse;
          mso-table-lspace: 0;
          mso-table-rspace: 0
        }
    
        img {
          border: 0;
          height: auto;
          line-height: 100%;
          outline: 0;
          text-decoration: none;
          -ms-interpolation-mode: bicubic
        }
    
        p {
          display: block;
          margin: 13px 0
        }
      </style>
      <!--[if !mso]><!-->
      <style type="text/css">
        @media only screen and (max-width:480px) {
          @-ms-viewport {
            width: 320px
          }
          @viewport {
            width: 320px
          }
        }
      </style>
      <!--<![endif]-->
      <!--[if mso]>
    <xml>
      <o:OfficeDocumentSettings>
        <o:AllowPNG/>
        <o:PixelsPerInch>96</o:PixelsPerInch>
      </o:OfficeDocumentSettings>
    </xml>
    <![endif]-->
      <!--[if lte mso 11]>
    <style type="text/css">
      .outlook-group-fix {
        width:100% !important;
      }
    </style>
    <![endif]-->
      <!--[if !mso]><!-->
      <link href="https://fonts.googleapis.com/css?family=Ubuntu:300,400,500,700" rel="stylesheet" type="text/css">
      <style type="text/css">
        @import url(https://fonts.googleapis.com/css?family=Ubuntu:300,400,500,700);
      </style>
      <!--<![endif]-->
      <style type="text/css">
        @media only screen and (min-width:480px) {
          .mj-column-per-66 {
            width: 66.66666666666666%!important
          }
          .mj-column-per-33 {
            width: 33.33333333333333%!important
          }
          .mj-column-per-100 {
            width: 100%!important
          }
          .mj-column-per-50 {
            width: 50%!important
          }
        }
      </style>
    </head>
    """

def emailHtmlFooter():
    return """
    </html>
    """