// This file is part of React-Invenio-Deposit
// Copyright (C) 2021 Graz University of Technology.
//
// Invenio-app-rdm is free software; you can redistribute it and/or modify it
// under the terms of the MIT License; see LICENSE file for more details.
// list of func used to
// mark the strings for translation
const funcList = ['i18next.t']
const extensions = ['.js', '.jsx']

module.exports = {
  options: {
    debug: true,
    removeUnusedKeys: true,
    browserLanguageDetection: true,
    func: {
      list: funcList,
      extensions: extensions,
    },
    //using Trans component
    trans: {
      component: 'Trans',
      extensions: extensions,
      fallbackKey: function (_ns, value) {
        return value
      },
    },
    ns: [
      // file name (.json)
      'translations',
    ],
    lngs: process.env.LANGUAGES.split(',') || ['en'],
    defaultLng: 'en',
    defaultNs: 'translations',
    // @param {string} lng The language currently used.
    // @param {string} ns The namespace currently used.
    // @param {string} key The translation key.
    // @return {string} Returns a default value for the translation key.
    defaultValue: function (lng, _ns, key) {
      if (lng === 'en') {
        // Return key as the default value for English language
        return key
      }
      return ''
    },
    resource: {
      // The path where resources get loaded from. Relative to current working directory.
      loadPath: 'messages/{{lng}}/LC_MESSAGES/{{ns}}.json',

      // The path to store resources.
      savePath: 'extracted-messages.json',
      jsonIndent: 2,
      lineEnding: '\n',
    },
    nsSeparator: false, // namespace separator

    //Set to false to disable key separator
    // if you prefer having keys as the fallback for translation (e.g. gettext).
    keySeparator: false,
  },
}
