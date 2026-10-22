#!/usr/bin/groovy
// SPDX-License-Identifier: BSD-2-Clause-Patent
// Copyright (c) 2022-2024 Intel Corporation

// To use a test branch (i.e. PR) until it lands to master
// I.e. for testing library changes
@Library(value='pipeline-lib@ryon-jensen/sre-4139-library-2daa588b1f22b38881676cfa46f45532d0178eef') _

packageBuildingPipelineDAOSTest(['distros': ['el8', 'el9', 'leap15'],
                                 'skip-build': false,
                                 'test-tag': 'daosio'])
