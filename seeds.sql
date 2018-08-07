-- Role --
INSERT INTO public.roles ("name", created_at, updated_at) VALUES('Admin', '2018-08-03 06:40:07.342', '2018-08-03 06:40:07.342');
INSERT INTO public.roles ("name", created_at, updated_at) VALUES('Writer', '2018-08-03 06:40:07.342', '2018-08-03 06:40:07.342');

-- User --
INSERT INTO public.users ("name", email, password, is_active, is_confirm, confirmation_token, remember_token, avatar, role_id, is_authenticated, last_authenticated, created_at, updated_at) VALUES('Admin', 'admin@admin.com', 'pbkdf2:sha256:50000$dl41vHyC$349b7c84072ea50e0c733c84e60c41cbde7e42093831b0e968156d3bab8def5f', true, true, '', '', NULL, 1, false, '2018-08-03 18:09:44.841', '2018-08-03 06:40:07.342', '2018-08-03 18:09:30.289');
INSERT INTO public.users ("name", email, password, is_active, is_confirm, confirmation_token, remember_token, avatar, role_id, is_authenticated, last_authenticated, created_at, updated_at) VALUES('Fachri Hawari', 'fachri.hawari@gmail.com', 'pbkdf2:sha256:50000$AcUCe0YA$b8a0b3ec4f1d6480722fcc5e1718c94c76b7807149dd0dfec99c6ed7ab537918', true, true, '', '', NULL, 2, false, NULL, '2018-08-03 06:40:07.342', '2018-08-03 06:40:07.342');

-- Menu --
INSERT INTO public.menus (label, target, parent_id, "position", "group", is_active, user_id, created_at, updated_at, icon) VALUES('Dashboard', '/', NULL, 1, 'admin.sidebar', true, 1, '2018-08-03 06:40:07.342', '2018-08-03 06:40:07.342', 'fa fa-dashboard');
INSERT INTO public.menus (label, target, parent_id, "position", "group", is_active, user_id, created_at, updated_at, icon) VALUES('Menu', '/menu/', NULL, 2, 'admin.sidebar', true, 1, '2018-08-03 06:40:07.342', '2018-08-03 06:40:07.342', 'fa fa-th');
INSERT INTO public.menus (label, target, parent_id, "position", "group", is_active, user_id, created_at, updated_at, icon) VALUES('Page', '/page/', NULL, 3, 'admin.sidebar', true, 1, '2018-08-03 06:40:07.342', '2018-08-03 06:40:07.342', 'fa fa-file');
INSERT INTO public.menus (label, target, parent_id, "position", "group", is_active, user_id, created_at, updated_at, icon) VALUES('User', '/user/', NULL, 4, 'admin.sidebar', true, 1, '2018-08-03 06:40:07.342', '2018-08-03 06:40:07.342', 'fa fa-user');
INSERT INTO public.menus (label, target, parent_id, "position", "group", is_active, user_id, created_at, updated_at, icon) VALUES('Role', '/role/', NULL, 5, 'admin.sidebar', true, 1, '2018-08-03 06:40:07.342', '2018-08-03 06:40:07.342', 'fa fa-file');

-- Permission --
INSERT INTO public.permissions ("name", "group", created_at, updated_at) VALUES('page.index', 'Page', '2018-08-03 06:40:07.342', '2018-08-03 06:40:07.342');
INSERT INTO public.permissions ("name", "group", created_at, updated_at) VALUES('page.create', 'Page', '2018-08-03 06:40:07.342', '2018-08-03 06:40:07.342');
INSERT INTO public.permissions ("name", "group", created_at, updated_at) VALUES('page.edit', 'Page', '2018-08-03 06:40:07.342', '2018-08-03 06:40:07.342');
INSERT INTO public.permissions ("name", "group", created_at, updated_at) VALUES('page.delete', 'Page', '2018-08-03 06:40:07.342', '2018-08-03 06:40:07.342');
INSERT INTO public.permissions ("name", "group", created_at, updated_at) VALUES('menu.index', 'Menu', '2018-08-03 06:40:07.342', '2018-08-03 06:40:07.342');
INSERT INTO public.permissions ("name", "group", created_at, updated_at) VALUES('menu.create', 'Menu', '2018-08-03 06:40:07.342', '2018-08-03 06:40:07.342');
INSERT INTO public.permissions ("name", "group", created_at, updated_at) VALUES('menu.edit', 'Menu', '2018-08-03 06:40:07.342', '2018-08-03 06:40:07.342');
INSERT INTO public.permissions ("name", "group", created_at, updated_at) VALUES('menu.delete', 'Menu', '2018-08-03 06:40:07.342', '2018-08-03 06:40:07.342');
INSERT INTO public.permissions ("name", "group", created_at, updated_at) VALUES('user.index', 'User', '2018-08-03 06:40:07.342', '2018-08-03 06:40:07.342');
INSERT INTO public.permissions ("name", "group", created_at, updated_at) VALUES('user.create', 'User', '2018-08-03 06:40:07.342', '2018-08-03 06:40:07.342');
INSERT INTO public.permissions ("name", "group", created_at, updated_at) VALUES('user.edit', 'User', '2018-08-03 06:40:07.342', '2018-08-03 06:40:07.342');
INSERT INTO public.permissions ("name", "group", created_at, updated_at) VALUES('user.delete', 'User', '2018-08-03 06:40:07.342', '2018-08-03 06:40:07.342');
INSERT INTO public.permissions ("name", "group", created_at, updated_at) VALUES('role.index', 'Role', '2018-08-03 06:40:07.342', '2018-08-03 06:40:07.342');
INSERT INTO public.permissions ("name", "group", created_at, updated_at) VALUES('role.create', 'Role', '2018-08-03 06:40:07.342', '2018-08-03 06:40:07.342');
INSERT INTO public.permissions ("name", "group", created_at, updated_at) VALUES('role.edit', 'Role', '2018-08-03 06:40:07.342', '2018-08-03 06:40:07.342');
INSERT INTO public.permissions ("name", "group", created_at, updated_at) VALUES('role.delete', 'Role', '2018-08-03 06:40:07.342', '2018-08-03 06:40:07.342');
INSERT INTO public.permissions ("name", "group", created_at, updated_at) VALUES('.index', 'Dashboard', '2018-08-03 06:40:07.342', '2018-08-03 06:40:07.342');

-- Role Permission --
INSERT INTO public.role_permission (role_id, permission_id, attached_at) VALUES(1, 1, '2018-08-03 06:40:07.342');
INSERT INTO public.role_permission (role_id, permission_id, attached_at) VALUES(1, 2, '2018-08-03 06:40:07.342');
INSERT INTO public.role_permission (role_id, permission_id, attached_at) VALUES(1, 3, '2018-08-03 06:40:07.342');
INSERT INTO public.role_permission (role_id, permission_id, attached_at) VALUES(1, 4, '2018-08-03 06:40:07.342');
INSERT INTO public.role_permission (role_id, permission_id, attached_at) VALUES(1, 5, '2018-08-03 06:40:07.342');
INSERT INTO public.role_permission (role_id, permission_id, attached_at) VALUES(1, 6, '2018-08-03 06:40:07.342');
INSERT INTO public.role_permission (role_id, permission_id, attached_at) VALUES(1, 7, '2018-08-03 06:40:07.342');
INSERT INTO public.role_permission (role_id, permission_id, attached_at) VALUES(1, 8, '2018-08-03 06:40:07.342');
INSERT INTO public.role_permission (role_id, permission_id, attached_at) VALUES(1, 9, '2018-08-03 06:40:07.342');
INSERT INTO public.role_permission (role_id, permission_id, attached_at) VALUES(1, 10, '2018-08-03 06:40:07.342');
INSERT INTO public.role_permission (role_id, permission_id, attached_at) VALUES(1, 11, '2018-08-03 06:40:07.342');
INSERT INTO public.role_permission (role_id, permission_id, attached_at) VALUES(1, 12, '2018-08-03 06:40:07.342');
INSERT INTO public.role_permission (role_id, permission_id, attached_at) VALUES(1, 13, '2018-08-03 06:40:07.342');
INSERT INTO public.role_permission (role_id, permission_id, attached_at) VALUES(1, 14, '2018-08-03 06:40:07.342');
INSERT INTO public.role_permission (role_id, permission_id, attached_at) VALUES(1, 15, '2018-08-03 06:40:07.342');
INSERT INTO public.role_permission (role_id, permission_id, attached_at) VALUES(1, 16, '2018-08-03 06:40:07.342');
INSERT INTO public.role_permission (role_id, permission_id, attached_at) VALUES(1, 17, '2018-08-03 06:40:07.342');