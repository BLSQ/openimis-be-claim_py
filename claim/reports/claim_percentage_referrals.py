from django.db import connection

from core.utils import get_nhia_logo
from tools.utils import dictfetchall

import logging

logger = logging.getLogger(__name__)

# If manually pasting from reportbro and you have test data, search and replace \" with \\"
template = """
{
  "docElements": [
    {
      "elementType": "text",
      "id": 3,
      "containerId": "0_header",
      "x": 0,
      "y": 20,
      "width": 575,
      "height": 40,
      "content": "Percentage of referrals in claims",
      "richText": false,
      "richTextContent": null,
      "richTextHtml": "",
      "eval": false,
      "styleId": "",
      "bold": true,
      "italic": false,
      "underline": false,
      "strikethrough": false,
      "horizontalAlignment": "center",
      "verticalAlignment": "middle",
      "textColor": "#006374",
      "backgroundColor": "",
      "font": "helvetica",
      "fontSize": "24",
      "lineSpacing": 1,
      "borderColor": "#000000",
      "borderWidth": 1,
      "borderAll": false,
      "borderLeft": false,
      "borderTop": false,
      "borderRight": false,
      "borderBottom": false,
      "paddingLeft": 2,
      "paddingTop": 2,
      "paddingRight": 2,
      "paddingBottom": 2,
      "printIf": "",
      "removeEmptyElement": false,
      "alwaysPrintOnSamePage": true,
      "pattern": "",
      "link": "",
      "cs_condition": "",
      "cs_styleId": "",
      "cs_bold": false,
      "cs_italic": false,
      "cs_underline": false,
      "cs_strikethrough": false,
      "cs_horizontalAlignment": "left",
      "cs_verticalAlignment": "top",
      "cs_textColor": "#000000",
      "cs_backgroundColor": "",
      "cs_font": "helvetica",
      "cs_fontSize": 12,
      "cs_lineSpacing": 1,
      "cs_borderColor": "#000000",
      "cs_borderWidth": "1",
      "cs_borderAll": false,
      "cs_borderLeft": false,
      "cs_borderTop": false,
      "cs_borderRight": false,
      "cs_borderBottom": false,
      "cs_paddingLeft": 2,
      "cs_paddingTop": 2,
      "cs_paddingRight": 2,
      "cs_paddingBottom": 2,
      "spreadsheet_hide": false,
      "spreadsheet_column": "",
      "spreadsheet_colspan": "",
      "spreadsheet_addEmptyRow": false,
      "spreadsheet_textWrap": false
    },
    {
      "elementType": "image",
      "id": 290,
      "containerId": "0_header",
      "x": 10,
      "y": 0,
      "width": 80,
      "height": 80,
      "source": "${nhia_logo}",
      "image": "",
      "imageFilename": "",
      "horizontalAlignment": "left",
      "verticalAlignment": "top",
      "backgroundColor": "",
      "printIf": "",
      "removeEmptyElement": false,
      "link": "",
      "spreadsheet_hide": false,
      "spreadsheet_column": "",
      "spreadsheet_addEmptyRow": false
    },
    {
      "elementType": "line",
      "id": 158,
      "containerId": "0_content",
      "x": 0,
      "y": 0,
      "width": 575,
      "height": 1,
      "color": "#000000",
      "printIf": ""
    },
    {
      "elementType": "text",
      "id": 193,
      "containerId": "0_content",
      "x": 0,
      "y": 10,
      "width": 575,
      "height": 20,
      "content": "List of health facilities, along with total number of claims, outpatient referrals total and inpatient referrals totals",
      "richText": false,
      "richTextContent": null,
      "richTextHtml": "",
      "eval": false,
      "styleId": "",
      "bold": true,
      "italic": false,
      "underline": true,
      "strikethrough": false,
      "horizontalAlignment": "center",
      "verticalAlignment": "top",
      "textColor": "#000000",
      "backgroundColor": "",
      "font": "helvetica",
      "fontSize": "10",
      "lineSpacing": 1,
      "borderColor": "#000000",
      "borderWidth": 1,
      "borderAll": false,
      "borderLeft": false,
      "borderTop": false,
      "borderRight": false,
      "borderBottom": false,
      "paddingLeft": 2,
      "paddingTop": 2,
      "paddingRight": 2,
      "paddingBottom": 2,
      "printIf": "",
      "removeEmptyElement": false,
      "alwaysPrintOnSamePage": true,
      "pattern": "",
      "link": "",
      "cs_condition": "",
      "cs_styleId": "",
      "cs_bold": false,
      "cs_italic": false,
      "cs_underline": false,
      "cs_strikethrough": false,
      "cs_horizontalAlignment": "left",
      "cs_verticalAlignment": "top",
      "cs_textColor": "#000000",
      "cs_backgroundColor": "",
      "cs_font": "helvetica",
      "cs_fontSize": 12,
      "cs_lineSpacing": 1,
      "cs_borderColor": "#000000",
      "cs_borderWidth": "1",
      "cs_borderAll": false,
      "cs_borderLeft": false,
      "cs_borderTop": false,
      "cs_borderRight": false,
      "cs_borderBottom": false,
      "cs_paddingLeft": 2,
      "cs_paddingTop": 2,
      "cs_paddingRight": 2,
      "cs_paddingBottom": 2,
      "spreadsheet_hide": false,
      "spreadsheet_column": "",
      "spreadsheet_colspan": "",
      "spreadsheet_addEmptyRow": false,
      "spreadsheet_textWrap": false
    },
    {
      "elementType": "table",
      "id": 272,
      "containerId": "0_content",
      "width": 574,
      "x": 0,
      "y": 40,
      "dataSource": "${data}",
      "columns": 4,
      "header": true,
      "contentRows": "1",
      "footer": false,
      "border": "grid",
      "borderColor": "#000000",
      "borderWidth": "1",
      "printIf": "",
      "removeEmptyElement": false,
      "spreadsheet_hide": false,
      "spreadsheet_column": "",
      "spreadsheet_addEmptyRow": false,
      "headerData": {
        "elementType": "none",
        "id": 273,
        "height": 20,
        "backgroundColor": "",
        "repeatHeader": false,
        "columnData": [
          {
            "elementType": "table_text",
            "id": 274,
            "width": 304,
            "content": "Health Facility",
            "eval": false,
            "colspan": "",
            "styleId": "",
            "bold": true,
            "italic": false,
            "underline": false,
            "strikethrough": false,
            "horizontalAlignment": "center",
            "verticalAlignment": "middle",
            "textColor": "#000000",
            "backgroundColor": "",
            "font": "helvetica",
            "fontSize": 12,
            "lineSpacing": 1,
            "paddingLeft": 2,
            "paddingTop": 2,
            "paddingRight": 2,
            "paddingBottom": 2,
            "pattern": "",
            "link": "",
            "cs_condition": "",
            "cs_styleId": "",
            "cs_bold": false,
            "cs_italic": false,
            "cs_underline": false,
            "cs_strikethrough": false,
            "cs_horizontalAlignment": "left",
            "cs_verticalAlignment": "top",
            "cs_textColor": "#000000",
            "cs_backgroundColor": "",
            "cs_font": "helvetica",
            "cs_fontSize": 12,
            "cs_lineSpacing": 1,
            "cs_paddingLeft": 2,
            "cs_paddingTop": 2,
            "cs_paddingRight": 2,
            "cs_paddingBottom": 2,
            "spreadsheet_textWrap": false,
            "printIf": "",
            "growWeight": 0,
            "borderWidth": 1
          },
          {
            "elementType": "table_text",
            "id": 275,
            "width": 90,
            "content": "Total Claims",
            "eval": false,
            "colspan": "",
            "styleId": "",
            "bold": true,
            "italic": false,
            "underline": false,
            "strikethrough": false,
            "horizontalAlignment": "center",
            "verticalAlignment": "middle",
            "textColor": "#000000",
            "backgroundColor": "",
            "font": "helvetica",
            "fontSize": 12,
            "lineSpacing": 1,
            "paddingLeft": 2,
            "paddingTop": 2,
            "paddingRight": 2,
            "paddingBottom": 2,
            "pattern": "",
            "link": "",
            "cs_condition": "",
            "cs_styleId": "",
            "cs_bold": false,
            "cs_italic": false,
            "cs_underline": false,
            "cs_strikethrough": false,
            "cs_horizontalAlignment": "left",
            "cs_verticalAlignment": "top",
            "cs_textColor": "#000000",
            "cs_backgroundColor": "",
            "cs_font": "helvetica",
            "cs_fontSize": 12,
            "cs_lineSpacing": 1,
            "cs_paddingLeft": 2,
            "cs_paddingTop": 2,
            "cs_paddingRight": 2,
            "cs_paddingBottom": 2,
            "spreadsheet_textWrap": false,
            "printIf": "",
            "growWeight": 0,
            "borderWidth": 1
          },
          {
            "elementType": "table_text",
            "id": 282,
            "width": 90,
            "content": "Referrals (OP)",
            "eval": false,
            "colspan": "",
            "styleId": "",
            "bold": true,
            "italic": false,
            "underline": false,
            "strikethrough": false,
            "horizontalAlignment": "center",
            "verticalAlignment": "middle",
            "textColor": "#000000",
            "backgroundColor": "",
            "font": "helvetica",
            "fontSize": 12,
            "lineSpacing": 1,
            "paddingLeft": 2,
            "paddingTop": 2,
            "paddingRight": 2,
            "paddingBottom": 2,
            "pattern": "",
            "link": "",
            "cs_condition": "",
            "cs_styleId": "",
            "cs_bold": false,
            "cs_italic": false,
            "cs_underline": false,
            "cs_strikethrough": false,
            "cs_horizontalAlignment": "left",
            "cs_verticalAlignment": "top",
            "cs_textColor": "#000000",
            "cs_backgroundColor": "",
            "cs_font": "helvetica",
            "cs_fontSize": 12,
            "cs_lineSpacing": 1,
            "cs_paddingLeft": 2,
            "cs_paddingTop": 2,
            "cs_paddingRight": 2,
            "cs_paddingBottom": 2,
            "spreadsheet_textWrap": false,
            "printIf": "",
            "growWeight": 0,
            "borderWidth": 1
          },
          {
            "elementType": "table_text",
            "id": 285,
            "width": 90,
            "content": "Referrals (IP)",
            "eval": false,
            "colspan": "",
            "styleId": "",
            "bold": true,
            "italic": false,
            "underline": false,
            "strikethrough": false,
            "horizontalAlignment": "center",
            "verticalAlignment": "middle",
            "textColor": "#000000",
            "backgroundColor": "",
            "font": "helvetica",
            "fontSize": 12,
            "lineSpacing": 1,
            "paddingLeft": 2,
            "paddingTop": 2,
            "paddingRight": 2,
            "paddingBottom": 2,
            "pattern": "",
            "link": "",
            "cs_condition": "",
            "cs_styleId": "",
            "cs_bold": false,
            "cs_italic": false,
            "cs_underline": false,
            "cs_strikethrough": false,
            "cs_horizontalAlignment": "left",
            "cs_verticalAlignment": "top",
            "cs_textColor": "#000000",
            "cs_backgroundColor": "",
            "cs_font": "helvetica",
            "cs_fontSize": 12,
            "cs_lineSpacing": 1,
            "cs_paddingLeft": 2,
            "cs_paddingTop": 2,
            "cs_paddingRight": 2,
            "cs_paddingBottom": 2,
            "spreadsheet_textWrap": false,
            "printIf": "",
            "growWeight": 0,
            "borderWidth": 1
          }
        ]
      },
      "contentDataRows": [
        {
          "elementType": "none",
          "id": 276,
          "height": 20,
          "backgroundColor": "",
          "alternateBackgroundColor": "",
          "groupExpression": "",
          "printIf": "",
          "alwaysPrintOnSamePage": true,
          "pageBreak": false,
          "repeatGroupHeader": false,
          "columnData": [
            {
              "elementType": "table_text",
              "id": 277,
              "width": 304,
              "content": "${hf}",
              "eval": false,
              "colspan": "",
              "styleId": "",
              "bold": false,
              "italic": false,
              "underline": false,
              "strikethrough": false,
              "horizontalAlignment": "left",
              "verticalAlignment": "middle",
              "textColor": "#000000",
              "backgroundColor": "",
              "font": "helvetica",
              "fontSize": 12,
              "lineSpacing": 1,
              "paddingLeft": 2,
              "paddingTop": 2,
              "paddingRight": 2,
              "paddingBottom": 2,
              "pattern": "",
              "link": "",
              "cs_condition": "",
              "cs_styleId": "",
              "cs_bold": false,
              "cs_italic": false,
              "cs_underline": false,
              "cs_strikethrough": false,
              "cs_horizontalAlignment": "left",
              "cs_verticalAlignment": "top",
              "cs_textColor": "#000000",
              "cs_backgroundColor": "",
              "cs_font": "helvetica",
              "cs_fontSize": 12,
              "cs_lineSpacing": 1,
              "cs_paddingLeft": 2,
              "cs_paddingTop": 2,
              "cs_paddingRight": 2,
              "cs_paddingBottom": 2,
              "spreadsheet_textWrap": false,
              "borderWidth": 1,
              "growWeight": 0
            },
            {
              "elementType": "table_text",
              "id": 278,
              "width": 90,
              "content": "${totalclaims}",
              "eval": false,
              "colspan": "",
              "styleId": "",
              "bold": false,
              "italic": false,
              "underline": false,
              "strikethrough": false,
              "horizontalAlignment": "center",
              "verticalAlignment": "middle",
              "textColor": "#000000",
              "backgroundColor": "",
              "font": "helvetica",
              "fontSize": 12,
              "lineSpacing": 1,
              "paddingLeft": 2,
              "paddingTop": 2,
              "paddingRight": 2,
              "paddingBottom": 2,
              "pattern": "",
              "link": "",
              "cs_condition": "",
              "cs_styleId": "",
              "cs_bold": false,
              "cs_italic": false,
              "cs_underline": false,
              "cs_strikethrough": false,
              "cs_horizontalAlignment": "left",
              "cs_verticalAlignment": "top",
              "cs_textColor": "#000000",
              "cs_backgroundColor": "",
              "cs_font": "helvetica",
              "cs_fontSize": 12,
              "cs_lineSpacing": 1,
              "cs_paddingLeft": 2,
              "cs_paddingTop": 2,
              "cs_paddingRight": 2,
              "cs_paddingBottom": 2,
              "spreadsheet_textWrap": false,
              "borderWidth": 1,
              "growWeight": 0
            },
            {
              "elementType": "table_text",
              "id": 283,
              "width": 90,
              "content": "${totalop}",
              "eval": false,
              "colspan": "",
              "styleId": "",
              "bold": false,
              "italic": false,
              "underline": false,
              "strikethrough": false,
              "horizontalAlignment": "center",
              "verticalAlignment": "middle",
              "textColor": "#000000",
              "backgroundColor": "",
              "font": "helvetica",
              "fontSize": 12,
              "lineSpacing": 1,
              "paddingLeft": 2,
              "paddingTop": 2,
              "paddingRight": 2,
              "paddingBottom": 2,
              "pattern": "",
              "link": "",
              "cs_condition": "",
              "cs_styleId": "",
              "cs_bold": false,
              "cs_italic": false,
              "cs_underline": false,
              "cs_strikethrough": false,
              "cs_horizontalAlignment": "left",
              "cs_verticalAlignment": "top",
              "cs_textColor": "#000000",
              "cs_backgroundColor": "",
              "cs_font": "helvetica",
              "cs_fontSize": 12,
              "cs_lineSpacing": 1,
              "cs_paddingLeft": 2,
              "cs_paddingTop": 2,
              "cs_paddingRight": 2,
              "cs_paddingBottom": 2,
              "spreadsheet_textWrap": false,
              "borderWidth": 1,
              "growWeight": 0
            },
            {
              "elementType": "table_text",
              "id": 286,
              "width": 90,
              "content": "${totalip}",
              "eval": false,
              "colspan": "",
              "styleId": "",
              "bold": false,
              "italic": false,
              "underline": false,
              "strikethrough": false,
              "horizontalAlignment": "center",
              "verticalAlignment": "middle",
              "textColor": "#000000",
              "backgroundColor": "",
              "font": "helvetica",
              "fontSize": 12,
              "lineSpacing": 1,
              "paddingLeft": 2,
              "paddingTop": 2,
              "paddingRight": 2,
              "paddingBottom": 2,
              "pattern": "",
              "link": "",
              "cs_condition": "",
              "cs_styleId": "",
              "cs_bold": false,
              "cs_italic": false,
              "cs_underline": false,
              "cs_strikethrough": false,
              "cs_horizontalAlignment": "left",
              "cs_verticalAlignment": "top",
              "cs_textColor": "#000000",
              "cs_backgroundColor": "",
              "cs_font": "helvetica",
              "cs_fontSize": 12,
              "cs_lineSpacing": 1,
              "cs_paddingLeft": 2,
              "cs_paddingTop": 2,
              "cs_paddingRight": 2,
              "cs_paddingBottom": 2,
              "spreadsheet_textWrap": false,
              "borderWidth": 1,
              "growWeight": 0
            }
          ]
        }
      ],
      "footerData": {
        "elementType": "none",
        "id": 279,
        "height": 20,
        "backgroundColor": "",
        "columnData": [
          {
            "elementType": "table_text",
            "id": 280,
            "width": 304,
            "content": "",
            "eval": false,
            "colspan": "",
            "styleId": "",
            "bold": false,
            "italic": false,
            "underline": false,
            "strikethrough": false,
            "horizontalAlignment": "left",
            "verticalAlignment": "top",
            "textColor": "#000000",
            "backgroundColor": "",
            "font": "helvetica",
            "fontSize": 12,
            "lineSpacing": 1,
            "paddingLeft": 2,
            "paddingTop": 2,
            "paddingRight": 2,
            "paddingBottom": 2,
            "pattern": "",
            "link": "",
            "cs_condition": "",
            "cs_styleId": "",
            "cs_bold": false,
            "cs_italic": false,
            "cs_underline": false,
            "cs_strikethrough": false,
            "cs_horizontalAlignment": "left",
            "cs_verticalAlignment": "top",
            "cs_textColor": "#000000",
            "cs_backgroundColor": "",
            "cs_font": "helvetica",
            "cs_fontSize": 12,
            "cs_lineSpacing": 1,
            "cs_paddingLeft": 2,
            "cs_paddingTop": 2,
            "cs_paddingRight": 2,
            "cs_paddingBottom": 2,
            "spreadsheet_textWrap": false,
            "borderWidth": 1,
            "growWeight": 0
          },
          {
            "elementType": "table_text",
            "id": 281,
            "width": 90,
            "content": "",
            "eval": false,
            "colspan": "",
            "styleId": "",
            "bold": false,
            "italic": false,
            "underline": false,
            "strikethrough": false,
            "horizontalAlignment": "left",
            "verticalAlignment": "top",
            "textColor": "#000000",
            "backgroundColor": "",
            "font": "helvetica",
            "fontSize": 12,
            "lineSpacing": 1,
            "paddingLeft": 2,
            "paddingTop": 2,
            "paddingRight": 2,
            "paddingBottom": 2,
            "pattern": "",
            "link": "",
            "cs_condition": "",
            "cs_styleId": "",
            "cs_bold": false,
            "cs_italic": false,
            "cs_underline": false,
            "cs_strikethrough": false,
            "cs_horizontalAlignment": "left",
            "cs_verticalAlignment": "top",
            "cs_textColor": "#000000",
            "cs_backgroundColor": "",
            "cs_font": "helvetica",
            "cs_fontSize": 12,
            "cs_lineSpacing": 1,
            "cs_paddingLeft": 2,
            "cs_paddingTop": 2,
            "cs_paddingRight": 2,
            "cs_paddingBottom": 2,
            "spreadsheet_textWrap": false,
            "borderWidth": 1,
            "growWeight": 0
          },
          {
            "elementType": "table_text",
            "id": 284,
            "width": 90,
            "content": "",
            "eval": false,
            "colspan": "",
            "styleId": "",
            "bold": false,
            "italic": false,
            "underline": false,
            "strikethrough": false,
            "horizontalAlignment": "left",
            "verticalAlignment": "top",
            "textColor": "#000000",
            "backgroundColor": "",
            "font": "helvetica",
            "fontSize": 12,
            "lineSpacing": 1,
            "paddingLeft": 2,
            "paddingTop": 2,
            "paddingRight": 2,
            "paddingBottom": 2,
            "pattern": "",
            "link": "",
            "cs_condition": "",
            "cs_styleId": "",
            "cs_bold": false,
            "cs_italic": false,
            "cs_underline": false,
            "cs_strikethrough": false,
            "cs_horizontalAlignment": "left",
            "cs_verticalAlignment": "top",
            "cs_textColor": "#000000",
            "cs_backgroundColor": "",
            "cs_font": "helvetica",
            "cs_fontSize": 12,
            "cs_lineSpacing": 1,
            "cs_paddingLeft": 2,
            "cs_paddingTop": 2,
            "cs_paddingRight": 2,
            "cs_paddingBottom": 2,
            "spreadsheet_textWrap": false,
            "borderWidth": 1,
            "growWeight": 0
          },
          {
            "elementType": "table_text",
            "id": 287,
            "width": 90,
            "content": "",
            "eval": false,
            "colspan": "",
            "styleId": "",
            "bold": false,
            "italic": false,
            "underline": false,
            "strikethrough": false,
            "horizontalAlignment": "left",
            "verticalAlignment": "top",
            "textColor": "#000000",
            "backgroundColor": "",
            "font": "helvetica",
            "fontSize": 12,
            "lineSpacing": 1,
            "paddingLeft": 2,
            "paddingTop": 2,
            "paddingRight": 2,
            "paddingBottom": 2,
            "pattern": "",
            "link": "",
            "cs_condition": "",
            "cs_styleId": "",
            "cs_bold": false,
            "cs_italic": false,
            "cs_underline": false,
            "cs_strikethrough": false,
            "cs_horizontalAlignment": "left",
            "cs_verticalAlignment": "top",
            "cs_textColor": "#000000",
            "cs_backgroundColor": "",
            "cs_font": "helvetica",
            "cs_fontSize": 12,
            "cs_lineSpacing": 1,
            "cs_paddingLeft": 2,
            "cs_paddingTop": 2,
            "cs_paddingRight": 2,
            "cs_paddingBottom": 2,
            "spreadsheet_textWrap": false,
            "borderWidth": 1,
            "growWeight": 0
          }
        ]
      }
    },
    {
      "elementType": "text",
      "id": 7,
      "containerId": "0_footer",
      "x": 320,
      "y": 0,
      "width": 255,
      "height": 30,
      "content": "Page ${page_number} / ${page_count}",
      "richText": false,
      "richTextContent": null,
      "richTextHtml": "",
      "eval": false,
      "styleId": "",
      "bold": false,
      "italic": false,
      "underline": false,
      "strikethrough": false,
      "horizontalAlignment": "right",
      "verticalAlignment": "middle",
      "textColor": "#666666",
      "backgroundColor": "",
      "font": "helvetica",
      "fontSize": 12,
      "lineSpacing": 1,
      "borderColor": "#000000",
      "borderWidth": 1,
      "borderAll": false,
      "borderLeft": false,
      "borderTop": false,
      "borderRight": false,
      "borderBottom": false,
      "paddingLeft": 2,
      "paddingTop": 2,
      "paddingRight": 2,
      "paddingBottom": 2,
      "printIf": "",
      "removeEmptyElement": false,
      "alwaysPrintOnSamePage": true,
      "pattern": "",
      "link": "",
      "cs_condition": "",
      "cs_styleId": "",
      "cs_bold": false,
      "cs_italic": false,
      "cs_underline": false,
      "cs_strikethrough": false,
      "cs_horizontalAlignment": "left",
      "cs_verticalAlignment": "top",
      "cs_textColor": "#000000",
      "cs_backgroundColor": "",
      "cs_font": "helvetica",
      "cs_fontSize": 12,
      "cs_lineSpacing": 1,
      "cs_borderColor": "#000000",
      "cs_borderWidth": "1",
      "cs_borderAll": false,
      "cs_borderLeft": false,
      "cs_borderTop": false,
      "cs_borderRight": false,
      "cs_borderBottom": false,
      "cs_paddingLeft": 2,
      "cs_paddingTop": 2,
      "cs_paddingRight": 2,
      "cs_paddingBottom": 2,
      "spreadsheet_hide": false,
      "spreadsheet_column": "",
      "spreadsheet_colspan": "",
      "spreadsheet_addEmptyRow": false,
      "spreadsheet_textWrap": false
    },
    {
      "elementType": "text",
      "id": 8,
      "containerId": "0_footer",
      "x": 0,
      "y": 0,
      "width": 350,
      "height": 30,
      "content": "Created on ${current_date} by ${requested_by}",
      "richText": false,
      "richTextContent": null,
      "richTextHtml": "",
      "eval": false,
      "styleId": "",
      "bold": false,
      "italic": false,
      "underline": false,
      "strikethrough": false,
      "horizontalAlignment": "left",
      "verticalAlignment": "middle",
      "textColor": "#666666",
      "backgroundColor": "",
      "font": "helvetica",
      "fontSize": 12,
      "lineSpacing": 1,
      "borderColor": "#000000",
      "borderWidth": 1,
      "borderAll": false,
      "borderLeft": false,
      "borderTop": false,
      "borderRight": false,
      "borderBottom": false,
      "paddingLeft": 2,
      "paddingTop": 2,
      "paddingRight": 2,
      "paddingBottom": 2,
      "printIf": "",
      "removeEmptyElement": false,
      "alwaysPrintOnSamePage": true,
      "pattern": "",
      "link": "",
      "cs_condition": "",
      "cs_styleId": "",
      "cs_bold": false,
      "cs_italic": false,
      "cs_underline": false,
      "cs_strikethrough": false,
      "cs_horizontalAlignment": "left",
      "cs_verticalAlignment": "top",
      "cs_textColor": "#000000",
      "cs_backgroundColor": "",
      "cs_font": "helvetica",
      "cs_fontSize": 12,
      "cs_lineSpacing": 1,
      "cs_borderColor": "#000000",
      "cs_borderWidth": "1",
      "cs_borderAll": false,
      "cs_borderLeft": false,
      "cs_borderTop": false,
      "cs_borderRight": false,
      "cs_borderBottom": false,
      "cs_paddingLeft": 2,
      "cs_paddingTop": 2,
      "cs_paddingRight": 2,
      "cs_paddingBottom": 2,
      "spreadsheet_hide": false,
      "spreadsheet_column": "",
      "spreadsheet_colspan": "",
      "spreadsheet_addEmptyRow": false,
      "spreadsheet_textWrap": false
    }
  ],
  "parameters": [
    {
      "id": 1,
      "name": "page_count",
      "type": "number",
      "arrayItemType": "string",
      "eval": false,
      "nullable": false,
      "pattern": "",
      "expression": "",
      "showOnlyNameType": true,
      "testData": ""
    },
    {
      "id": 2,
      "name": "page_number",
      "type": "number",
      "arrayItemType": "string",
      "eval": false,
      "nullable": false,
      "pattern": "",
      "expression": "",
      "showOnlyNameType": true,
      "testData": ""
    },
    {
      "id": 9,
      "name": "current_date",
      "type": "date",
      "arrayItemType": "string",
      "eval": false,
      "nullable": false,
      "pattern": "d/M/yyyy H:mm",
      "expression": "",
      "showOnlyNameType": false,
      "testData": ""
    },
    {
      "id": 233,
      "name": "data",
      "type": "array",
      "arrayItemType": "string",
      "eval": false,
      "nullable": false,
      "pattern": "",
      "expression": "",
      "showOnlyNameType": false,
      "testData": "",
      "children": [
        {
          "id": 234,
          "name": "row_number",
          "type": "number",
          "arrayItemType": "string",
          "eval": false,
          "nullable": false,
          "pattern": "",
          "expression": "",
          "showOnlyNameType": true,
          "testData": ""
        },
        {
          "id": 235,
          "name": "hf",
          "type": "string",
          "arrayItemType": "string",
          "eval": false,
          "nullable": false,
          "pattern": "",
          "expression": "",
          "showOnlyNameType": false,
          "testData": ""
        },
        {
          "id": 236,
          "name": "totalclaims",
          "type": "number",
          "arrayItemType": "string",
          "eval": false,
          "nullable": true,
          "pattern": "#,##0",
          "expression": "",
          "showOnlyNameType": false,
          "testData": ""
        },
        {
          "id": 262,
          "name": "totalop",
          "type": "number",
          "arrayItemType": "string",
          "eval": false,
          "nullable": true,
          "pattern": "#,##0",
          "expression": "",
          "showOnlyNameType": false,
          "testData": ""
        },
        {
          "id": 271,
          "name": "totalip",
          "type": "number",
          "arrayItemType": "string",
          "eval": false,
          "nullable": true,
          "pattern": "#,##0",
          "expression": "",
          "showOnlyNameType": false,
          "testData": ""
        }
      ]
    },
    {
      "id": 288,
      "name": "nhia_logo",
      "type": "image",
      "arrayItemType": "string",
      "eval": false,
      "nullable": false,
      "pattern": "",
      "expression": "",
      "showOnlyNameType": false,
      "testData": ""
    },
    {
      "id": 289,
      "name": "requested_by",
      "type": "string",
      "arrayItemType": "string",
      "eval": false,
      "nullable": false,
      "pattern": "",
      "expression": "",
      "showOnlyNameType": false,
      "testData": ""
    }
  ],
  "styles": [
    {
      "id": 33,
      "name": "Table Header",
      "bold": true,
      "italic": false,
      "underline": false,
      "strikethrough": false,
      "horizontalAlignment": "left",
      "verticalAlignment": "middle",
      "textColor": "#000000",
      "backgroundColor": "",
      "font": "helvetica",
      "fontSize": "12",
      "lineSpacing": 1,
      "borderColor": "#000000",
      "borderWidth": "1",
      "borderAll": false,
      "borderLeft": false,
      "borderTop": false,
      "borderRight": false,
      "borderBottom": false,
      "paddingLeft": "2",
      "paddingTop": "2",
      "paddingRight": "2",
      "paddingBottom": "2"
    },
    {
      "id": 34,
      "name": "Table Content",
      "bold": false,
      "italic": false,
      "underline": false,
      "strikethrough": false,
      "horizontalAlignment": "left",
      "verticalAlignment": "middle",
      "textColor": "#000000",
      "backgroundColor": "",
      "font": "helvetica",
      "fontSize": "9",
      "lineSpacing": 1,
      "borderColor": "#000000",
      "borderWidth": "1",
      "borderAll": false,
      "borderLeft": false,
      "borderTop": false,
      "borderRight": false,
      "borderBottom": false,
      "paddingLeft": "2",
      "paddingTop": "2",
      "paddingRight": "2",
      "paddingBottom": "2"
    },
    {
      "id": 35,
      "name": "Table Content Highlight",
      "bold": true,
      "italic": false,
      "underline": false,
      "strikethrough": false,
      "horizontalAlignment": "center",
      "verticalAlignment": "middle",
      "textColor": "#3d85c6",
      "backgroundColor": "",
      "font": "helvetica",
      "fontSize": "9",
      "lineSpacing": 1,
      "borderColor": "#000000",
      "borderWidth": "1",
      "borderAll": false,
      "borderLeft": false,
      "borderTop": false,
      "borderRight": false,
      "borderBottom": false,
      "paddingLeft": "2",
      "paddingTop": "2",
      "paddingRight": "2",
      "paddingBottom": "2"
    }
  ],
  "version": 3,
  "documentProperties": {
    "pageFormat": "A4",
    "pageWidth": "",
    "pageHeight": "",
    "unit": "mm",
    "orientation": "portrait",
    "contentHeight": "",
    "marginLeft": "10",
    "marginTop": "10",
    "marginRight": "10",
    "marginBottom": "10",
    "header": true,
    "headerSize": "80",
    "headerDisplay": "always",
    "footer": true,
    "footerSize": "30",
    "footerDisplay": "always",
    "patternLocale": "en",
    "patternCurrencySymbol": "$"
  }
}
"""

# TODO transform the SQL query into a Django ORM query
percentage_referrals_sql = """
SELECT CONCAT(HF."HFCode", ' - ', HF."HFName") HF, TotalClaim.TotalClaims, RefOP.TotalOP, RefIP.TotalIP
FROM (SELECT HF."HfID", HF."HFCode", HF."HFName"
      FROM "tblHF" HF
               INNER JOIN "uvwLocations" L ON L."LocationId" = HF."LocationId"
      WHERE HF."ValidityTo" Is NULL
        AND HF."HFLevel" IN ('D', 'C')
        AND (L."RegionId" = %(region_id)s OR %(region_id)s = 0 OR L."LocationId" IS NULL)
        AND (L."DistrictId" = %(district_id)s OR %(district_id)s = 0 OR L."DistrictId" IS NULL)
      ) HF
         LEFT OUTER JOIN (SELECT COUNT(1) TotalClaims, "HFID"
                          FROM "tblClaim"
                          WHERE "ValidityTo" Is NULL
                          AND "DateClaimed" BETWEEN %(date_start)s AND %(date_end)s
                          GROUP BY "HFID") TotalClaim ON HF."HfID" = TotalClaim."HFID"
         LEFT OUTER JOIN (SELECT I."HFID", COUNT(C."ClaimID") TotalOP
                          FROM "tblClaim" C
                                   INNER JOIN "tblInsuree" I ON C."InsureeID" = I."InsureeID"
                                   INNER JOIN "tblHF" HF ON C."HFID" = HF."HfID"
                                   INNER JOIN "uvwLocations" L ON L."LocationId" = HF."LocationId"
                          WHERE C."ValidityTo" Is NULL
                            AND I."ValidityTo" IS NULL
                            AND HF."ValidityTo" IS NULL
                            AND (C."DateTo" is null OR C."DateFrom" = C."DateTo")
                            AND HF."HfID" <> I."HFID"
                            AND C."VisitType" = N'R'
                            AND (L."RegionId" = %(region_id)s OR %(region_id)s = 0 OR L."LocationId" IS NULL)
                            AND (L."DistrictId" = %(district_id)s OR %(district_id)s = 0 OR L."DistrictId" IS NULL)
                            AND C."DateClaimed" BETWEEN %(date_start)s AND %(date_end)s
                          GROUP BY I."HFID") RefOP ON HF."HfID" = RefOP."HFID"
         LEFT OUTER JOIN (SELECT I."HFID", COUNT(C."ClaimID") TotalIP
                          FROM "tblClaim" C
                                   INNER JOIN "tblInsuree" I ON C."InsureeID" = I."InsureeID"
                                   INNER JOIN "tblHF" HF ON C."HFID" = HF."HfID"
                                   INNER JOIN "uvwLocations" L ON L."LocationId" = HF."LocationId"
                          WHERE C."ValidityTo" Is NULL
                            AND I."ValidityTo" IS NULL
                            AND HF."ValidityTo" IS NULL
                            AND C."DateTo" is not null and C."DateFrom" <> C."DateTo"
                            AND HF."HfID" <> I."HFID"
                            AND C."VisitType" = N'R'
                            AND (L."RegionId" = %(region_id)s OR %(region_id)s = 0 OR L."LocationId" IS NULL)
                            AND (L."DistrictId" = %(district_id)s OR %(district_id)s = 0 OR L."DistrictId" IS NULL)
                            AND C."DateClaimed" BETWEEN %(date_start)s AND %(date_end)s
                          GROUP BY I."HFID") RefIP ON HF."HfID" = RefIP."HFID"
"""


def claim_percentage_referrals_query(user, region_id=0, district_id=0, date_start="2019-01-01", date_end="2022-12-31",
                                     **kwargs):
    with connection.cursor() as cur:
        try:
            cur.execute(
                percentage_referrals_sql,
                {
                    "region_id": region_id,
                    "district_id": district_id,
                    "date_start": date_start,
                    "date_end": date_end,
                },
            )
            data = dictfetchall(cur)
            return {
                "data": data,
                "nhia_logo": get_nhia_logo(),
                "requested_by": f"{user.username} - {user.other_names} {user.last_name}",
            }
        except Exception as e:
            logger.exception("Error fetching claim percentage referrals query")
            raise e

    logger.error("Claim percentage referrals query arrived at end of function")
    return {"data": None}
