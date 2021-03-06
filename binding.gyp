{
  'target_defaults': {
    'conditions': [
      ['OS=="linux"', {
        'cflags_cc!': [ '-fno-exceptions', '-fno-rtti' ],
        'defines': [ '_REENTRANT', 'ACE_HAS_AIO_CALLS', '_GNU_SOURCE',
                      'ACE_HAS_EXCEPTIONS', '__ACE_INLINE__' ],
      }],
      ['OS=="win"', {
        'msvs_settings': {
          'VCCLCompilerTool': {
            'RuntimeTypeInfo': 'true',
          },
        },
        'configurations': {
          'Debug': {
            'msvs_settings': {
              'VCCLCompilerTool': {
                'RuntimeLibrary': '3',
                'ExceptionHandling': '1',  
              },
            },
          },
          'Release': {
            'msvs_settings': {
              'VCCLCompilerTool': {
                'RuntimeLibrary': '2',
                'ExceptionHandling': '1',  
              },
            },
          },
        },
      }],
    ],
  },
  'targets': [
    {
      'target_name': 'node_opendds',
      'sources': [ 'src/node-opendds.cpp',
                   'src/NodeDRListener.cpp',
                   'src/NodeQosConversion.cpp' ],
      'include_dirs': [ "<!(node -e \"require('nan')\")",
                      '$(ACE_ROOT)', '$(TAO_ROOT)', '$(DDS_ROOT)' ],
      'cflags!': [ '-fno-exceptions' ],
      'cflags_cc!': [ '-fno-exceptions' ],                
      'conditions': [
        ['OS=="linux"', {
          'link_settings': {
            'libraries': [ '-lOpenDDS_Dcps', '-lTAO_PortableServer',
                           '-lTAO_AnyTypeCode', '-lTAO', '-lACE' ],
            'ldflags': [ '-L$(ACE_ROOT)/lib', '-L$(DDS_ROOT)/lib' ],
          },
        }],
        [ "OS==\"mac\"", {
            "xcode_settings": {
              "OTHER_CFLAGS": [
                "-mmacosx-version-min=10.7",
                "-std=c++11",
                "-stdlib=libc++"
              ],
              "GCC_ENABLE_CPP_RTTI": "YES",
              "GCC_ENABLE_CPP_EXCEPTIONS": "YES"
            }
          }],
        ['OS=="win"', {
          'msvs_settings' : {
            'VCLinkerTool': {
              'AdditionalLibraryDirectories': [ '$(ACE_ROOT)/lib',
                                                '$(DDS_ROOT)/lib' ],
            },
          },
          'link_settings': {
            'libraries': [ 'OpenDDS_Dcps<(lib_suffix)',
                           'TAO_PortableServer<(lib_suffix)',
                           'TAO_AnyTypeCode<(lib_suffix)',
                           'TAO<(lib_suffix)', 'ACE<(lib_suffix)' ],
          },
        }]
      ],
    }
  ]
}
